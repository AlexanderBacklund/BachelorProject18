package com.example.baurre95.my_first_kotlin

import android.content.Context
import android.Manifest
import android.content.pm.PackageManager
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.os.Environment
import android.support.v4.app.ActivityCompat
import android.support.v4.content.ContextCompat
import android.util.Log
import android.view.View
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_file.*
import java.io.*
import java.util.*
import kotlin.collections.ArrayList


class file : AppCompatActivity() {
    companion object {
        const val REQUEST_PERMISSION = 1
    }

    val FILENAME = "test"
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_file)
        save.setOnClickListener{}

        var wifiListCSV = intent.getStringArrayListExtra("array_list")
        Log.d("AlexanderBacklund", wifiListCSV.toString())

        if(wifiListCSV != null) {
            tv.text = wifiListCSV[1].toString()
        }
        else{
            tv.text = "null"
        }
        save.setOnClickListener{
            val path = getExternalFilesDir(null)
            val letDirectory = File(path,"LET")
            letDirectory.mkdirs()
            val file = File(letDirectory, "records.txt")
            FileOutputStream(file).use {
                it.write(wifiListCSV.toString().toByteArray())
            }

            Toast.makeText(this, path.toString(),Toast.LENGTH_SHORT).show()
        }
    }
}

