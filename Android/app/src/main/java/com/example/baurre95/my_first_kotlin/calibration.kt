package com.example.baurre95.my_first_kotlin

import android.Manifest.permission.ACCESS_FINE_LOCATION
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.content.pm.PackageManager
import android.net.wifi.ScanResult
import android.net.wifi.WifiManager
import android.os.Build
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.util.Log
import android.widget.ArrayAdapter
import kotlinx.android.synthetic.main.activity_calibration.*



class calibration : AppCompatActivity() {

    val REQUEST_FINE_LOCATION: Int=0
    var resultList = ArrayList<ScanResult>()
    val axisList = ArrayList<String>()
    lateinit var wifiManager: WifiManager

    val broadcastReceiver = object : BroadcastReceiver() {
        override fun onReceive(contxt: Context?, intent: Intent?) {
            resultList = wifiManager.scanResults as ArrayList<ScanResult>
            Log.d("TESTING", "onReceive Called")
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_calibration)

        wifiManager = this.applicationContext.getSystemService(Context.WIFI_SERVICE) as WifiManager

        scan.setOnClickListener {
            startScanning()
        }

        export.setOnClickListener{
            val intent = Intent(this, file::class.java)
            if(axisList.size != 0) {
                intent.putExtra("array_list", axisList)
            }
            startActivity(intent)
        }

    }


    fun startScanning(){
        wifiManager.setWifiEnabled(true)
        registerReceiver(broadcastReceiver, IntentFilter(WifiManager.SCAN_RESULTS_AVAILABLE_ACTION))
        val enabled: Boolean = wifiManager.isWifiEnabled()
        mayRequestLocation()
        wifiManager.startScan()

        Handler().postDelayed({
            this.stopScanning()
        }, 5000)
    }

    fun stopScanning() {
        unregisterReceiver(broadcastReceiver)
        resultList.sortedWith(compareBy({ it.level }))
        for (i in 0..resultList.size) {
            axisList.add(resultList[i].SSID+" "+resultList[i].BSSID+" "+resultList[i].level)
            if(i == 10) {
                break
            }
        }
        val adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, axisList)
        listView_bssid.adapter = adapter
        Log.d("TESTING", axisList.toString())

    }
    private fun mayRequestLocation(): Boolean {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.M) {
            return true
        }
        if (checkSelfPermission(ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED) {
            return true
        }
        if (shouldShowRequestPermissionRationale(ACCESS_FINE_LOCATION)) {
            requestPermissions(arrayOf(ACCESS_FINE_LOCATION), REQUEST_FINE_LOCATION)

        } else {
            requestPermissions(arrayOf(ACCESS_FINE_LOCATION), REQUEST_FINE_LOCATION)
        }
        return false
    }
//    private fun sortScanResultsAfterSignal(scn: ArrayList<ScanResult>): ArrayList<ScanResult> {
//        val newlist= ArrayList<ScanResult>()
//        var r = scn[0]
//        var i: Int = 0
//        for (res in scn){
//            if (res.level > r.level && i < 3) {
//                r = res
//                i++
//            }
//        }
//        newlist.add(r)
//
//
//        return newlist
//    }


}