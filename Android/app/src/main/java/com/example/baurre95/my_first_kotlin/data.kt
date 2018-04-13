package com.example.baurre95.my_first_kotlin

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.util.Log
import android.widget.ArrayAdapter
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_data.*
import java.io.File
import java.io.FileOutputStream

class data : AppCompatActivity() {
    val FILENAME = "accesspoints.txt"
    var myList =  listOf<String>()

    fun printFromFile(file: File) {
        myList = file.readLines()
        Log.d("TESTING", myList.toString())
        val adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, myList)
        APlv.adapter = adapter
    }

    fun writeToFile(file: File,text: String) {
        file.appendText(text)

    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_data)
        val path = getExternalFilesDir(null)

        val filecheck = File(path.toString() +  "/" + "Saved Files"+ "/" + FILENAME)

        if (filecheck.exists()) {
            Toast.makeText(this, "File exists", Toast.LENGTH_SHORT).show()

        }
        else {
            val letDirectory = File(path,"Saved Files")
            letDirectory.mkdirs()
            val file = File(letDirectory, FILENAME)
            writeToFile(file, "a")
        }
        printFromFile(filecheck)



        APaddbtn.setOnClickListener{
            FileOutputStream(filecheck).use {
                var textFromET = APet.text.toString()
                writeToFile(filecheck, textFromET)
                Handler().postDelayed({
                }, 500)
                printFromFile(filecheck)
            }
        }
    }
}


