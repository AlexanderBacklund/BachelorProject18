package com.example.baurre95.my_first_kotlin

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import com.example.baurre95.my_first_kotlin.R.id.*
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)


        calbtn.setOnClickListener{
            val calintent = Intent(this, calibration::class.java)
            startActivity(calintent)
        }

        databtn.setOnClickListener{
            val dataintent = Intent(this, data::class.java)
            startActivity(dataintent)
        }

        guidebtn.setOnClickListener{
            val guideintent = Intent(this, guide::class.java)
            startActivity(guideintent)
        }
    }
}
