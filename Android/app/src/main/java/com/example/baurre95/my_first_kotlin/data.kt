package com.example.baurre95.my_first_kotlin

import android.Manifest
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
import android.widget.PopupMenu
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_data.*
import java.io.File

class data : AppCompatActivity() {
    val filenameToDB = "accesspointsToDb.csv"
    val filenameToUsers = "ReferencePointsToUser.csv"

    var myList =  listOf<String>()

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

    fun printFromFile(file: File) {
        myList = file.readLines()
        val adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, myList)
        APlv.adapter = adapter
    }

    fun writeToFile(file: File,text: String) {
        file.appendText(text)

    }
    fun startScanning(file: File){
        if (resultList.size > 0 || axisList.size > 0) {
            resultList.clear()
            axisList.clear()
        }

        wifiManager.setWifiEnabled(true)
        registerReceiver(broadcastReceiver, IntentFilter(WifiManager.SCAN_RESULTS_AVAILABLE_ACTION))
        val enabled: Boolean = wifiManager.isWifiEnabled()
        mayRequestLocation()
        wifiManager.startScan()

        Handler().postDelayed({
            this.stopScanning(file)
        }, 5000)
    }

    fun stopScanning(file: File) {
        unregisterReceiver(broadcastReceiver)
        try {
            resultList.sortedWith(compareBy({ it.level }))
            for (i in 0..resultList.size) {
                axisList.add(resultList[i].SSID+" "+resultList[i].BSSID+" "+resultList[i].level)
                if(i == 10) {
                    break
                }
            }
            var textToDB = ""
            for (i in 0..axisList.size) {
                textToDB +="\n" + axisList[i]
                writeToFile(file, textToDB)
            }
        } catch (e: IndexOutOfBoundsException) {
            Toast.makeText(this, "Scan Failed", Toast.LENGTH_SHORT).show()

        }


    }
    private fun mayRequestLocation(): Boolean {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.M) {
            return true
        }
        if (checkSelfPermission(Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED) {
            return true
        }
        if (shouldShowRequestPermissionRationale(Manifest.permission.ACCESS_FINE_LOCATION)) {
            requestPermissions(arrayOf(Manifest.permission.ACCESS_FINE_LOCATION), REQUEST_FINE_LOCATION)

        } else {
            requestPermissions(arrayOf(Manifest.permission.ACCESS_FINE_LOCATION), REQUEST_FINE_LOCATION)
        }
        return false
    }


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_data)

        wifiManager = this.applicationContext.getSystemService(Context.WIFI_SERVICE) as WifiManager

        val path = getExternalFilesDir(null)
        val filecheckDB = File(path.toString() +  "/" + "Saved Files"+ "/" + filenameToDB)
        val filecheckUser = File(path.toString() +  "/" + "Saved Files"+ "/" + filenameToUsers)

        if (filecheckDB.exists()) {
            Toast.makeText(this, "File DB exists", Toast.LENGTH_SHORT).show()
        }
        else {
            val letDirectory = File(path,"Saved Files")
            letDirectory.mkdirs()
            val file = File(letDirectory, filenameToDB)
            writeToFile(file, "a")
        }

        if (filecheckUser.exists()) {
            Toast.makeText(this, "File user exists", Toast.LENGTH_SHORT).show()
        }
        else {
            val letDirectory = File(path,"Saved Files")
            letDirectory.mkdirs()
            val file2 = File(letDirectory, filenameToUsers)
            writeToFile(file2, "a")
        }

        printFromFile(filecheckUser)

        APlv.setOnItemClickListener {parent, view, position, id ->
            val popupMenu = PopupMenu(this, view)
            popupMenu.setOnMenuItemClickListener { item  ->
                when (item.itemId) {
                    R.id.menu_start_scan -> {
                        startScanning(filecheckDB)
                        Toast.makeText(this, "Klart", Toast.LENGTH_LONG).show()
                        true
                    }
                    R.id.menu_delete -> {
                        Toast.makeText(this, "delete", Toast.LENGTH_LONG).show()
                        true
                    }
                    else -> false
                }
            }
            popupMenu.inflate(R.menu.menu_main)
            popupMenu.show()

            //Toast.makeText(this, "Position Clicked:"+" "+position,Toast.LENGTH_SHORT).show()
        }


        APaddbtn.setOnClickListener{
            var textFromET = APet.text.toString()
            textFromET += "\n"
            writeToFile(filecheckUser, textFromET)
            writeToFile(filecheckDB, textFromET)

            printFromFile(filecheckUser)

        }
    }
}


