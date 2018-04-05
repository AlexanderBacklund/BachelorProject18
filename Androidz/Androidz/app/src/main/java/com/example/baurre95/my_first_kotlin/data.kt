package com.example.baurre95.my_first_kotlin

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_data.*
import java.io.FileWriter
import java.io.IOException



class data : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_data)

        /*val CSV_HEADER = "id,name,address,age"

        fun main() {
            var fileWriter: FileWriter? = null

            try {
                fileWriter = FileWriter("customer.csv")

                fileWriter.append(CSV_HEADER)
                fileWriter.append('\n')

                println("Write CVS, worked!")

            } catch (e: Exception) {
                println("Writing CSV error!")
                e.printStackTrace()
            } finally {
                try {
                    fileWriter!!.flush()
                    fileWriter.close()
                } catch (e: IOException) {
                    println("Flushing/closing error!")
                    e.printStackTrace()
                }
            }
        }*/




        exp.setOnClickListener{
            val fileintent = Intent(this, file::class.java)
            startActivity(fileintent)

        }
    }
}


