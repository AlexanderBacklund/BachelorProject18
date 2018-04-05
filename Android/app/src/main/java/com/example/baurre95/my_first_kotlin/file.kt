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

    var FILENAME = "test.txt"
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_file)
        save.setOnClickListener{}

        var lalal = intent.getStringArrayListExtra("array_list")
        Log.d("AlexanderBacklund", lalal.toString())

        //val myValue = intent.getStringExtra("array_list")
        if(lalal != null) {
          //  tv.setOnClickListener {
        tv.text = lalal[1].toString()
        }
        else{
            tv.text = "null"
        }
    }
}

