package com.example.baurre95.my_first_kotlin

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_file.*
import java.io.*

class file : AppCompatActivity() {
    companion object {
        const val REQUEST_PERMISSION = 1
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_file)
        save.setOnClickListener{}

        var wifiListCSV = intent.getStringArrayListExtra("array_list")

        if(wifiListCSV != null) {
            tv.text = wifiListCSV[1].toString()
        }
        else{
            tv.text = "null"
        }
        save.setOnClickListener{
            val path = getExternalFilesDir(null)
            val letDirectory = File(path,"Saved Files")
            letDirectory.mkdirs()
            val file = File(letDirectory, "records.csv")
            FileOutputStream(file).use {
                it.write(wifiListCSV.toString().toByteArray())
            }

            Toast.makeText(this, path.toString(),Toast.LENGTH_SHORT).show()
        }
    }
}

