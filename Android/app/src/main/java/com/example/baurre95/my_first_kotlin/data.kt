package com.example.baurre95.my_first_kotlin

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.ArrayAdapter
import android.widget.PopupMenu
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_data.*
import java.io.File

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

        APlv.setOnItemClickListener {parent, view, position, id ->
            val popupMenu = PopupMenu(this, view)
            popupMenu.setOnMenuItemClickListener { item  ->
                when (item.itemId) {
                    R.id.menu_start_scan -> {
                        val intent = Intent(this, calibration::class.java)
                        startActivity(intent)
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

            Toast.makeText(this, "Position Clicked:"+" "+position,Toast.LENGTH_SHORT).show()
        }


        APaddbtn.setOnClickListener{
            var textFromET = APet.text.toString()
            textFromET += "\n"
            writeToFile(filecheck, textFromET)

            printFromFile(filecheck)

        }
    }
}


