package com.example.baurre95.my_first_kotlin

import android.content.Context
import android.Manifest
import android.content.pm.PackageManager
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.os.Environment
import android.support.v4.app.ActivityCompat
import android.support.v4.content.ContextCompat
import android.view.View
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_file.*
import java.io.*
import java.util.*


class file : AppCompatActivity() {
    companion object {
        const val REQUEST_PERMISSION = 1
    }

    var FILENAME = "test.txt"
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_file)
        save.setOnClickListener{write()}

    }

        override fun onStart() {
            super.onStart()
            if (ContextCompat.checkSelfPermission(this, Manifest.permission.WRITE_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED) {
                ActivityCompat.requestPermissions(this, arrayOf(Manifest.permission.WRITE_EXTERNAL_STORAGE), REQUEST_PERMISSION)
            } else {
                write()
            }
        }

        override fun onRequestPermissionsResult(requestCode: Int, permissions: Array<out String>, grantResults: IntArray) {
            when (requestCode) {
                REQUEST_PERMISSION -> if (grantResults.size > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                    write()
                }
            }
        }

        fun write() {
            val dir = "${Environment.getExternalStorageDirectory()}/$packageName"
            File(dir).mkdirs()
            val file = "%1\$tY%1\$tm%1\$td%1\$tH%1\$tM%1\$tS.log".format(Date())
            File("$dir/$file").printWriter().use {
                it.println("textenlalaas")
            }
        }



        /*        val context = applicationContext

        val path = context.filesDir

        val letDirectory = File(path, "LET")
        letDirectory.mkdirs()

        val file = File(letDirectory, "test.txt")


        val stringen: String = "hejsanhoppsanfallerallera "
        file.writeText(stringen)

        //val inputAsString = FileInputStream(file).bufferedReader().use { it.readText() }
*/
   }
