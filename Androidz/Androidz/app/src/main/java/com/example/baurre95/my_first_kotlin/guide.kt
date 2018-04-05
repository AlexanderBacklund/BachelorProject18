package com.example.baurre95.my_first_kotlin

import android.support.v7.app.AppCompatActivity
import android.os.Bundle

import kotlinx.android.synthetic.main.activity_guide.*

class guide : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_guide)

        textviewalex.setText("hej, här kommer det en massa text om hur appen kommer att fungera och så ! :D ")
    }


}
