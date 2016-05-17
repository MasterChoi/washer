package com.example.administrator.washerboo_application;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;

/**
 * Created by Administrator on 2015-11-15.
 */
public class ResultView extends Activity {
    String dataInput;
    ImageView resultImage;
    Button resetBtn;
    Socket socket;
    BufferedReader socket_in;
    String data;
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.resultview);
        Log.d("AAAAAAAAAAAAAAAA", "11111111111");
        worker.start();
        Log.d("AAAAAAAAAAAAAAAA", "2222222222222222");
        resultImage=(ImageView)findViewById(R.id.resultimage);
        resetBtn = (Button)findViewById(R.id.resetBtn);
        Log.d("AAAAAAAAAAAAAAAA","33333333333333333331");
        try { Thread.sleep(1000);} catch (Exception e){}
        switch (dataInput){
            case "1":
                resultImage.setImageResource(R.drawable.isusing);
                break;
            case "2":
                resultImage.setImageResource(R.drawable.unempty);
                break;
            case "3":
                resultImage.setImageResource(R.drawable.isempty);
                break;
            default:
                break;
        }

        resetBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                switch (dataInput){
                    case "1":
                        resultImage.setImageResource(R.drawable.isusing);
                        break;
                    case "2":
                        resultImage.setImageResource(R.drawable.unempty);
                        break;
                    case "3":
                        resultImage.setImageResource(R.drawable.isempty);
                        break;
                    default:
                        break;
                }
            }
        });
    }

    Thread worker = new Thread() {
        public void run() {
            while(true)
            try {
                Log.d("before create socket", "before create socket");
                socket = new Socket("52.69.56.103",5555);
                Log.d("after create socket","after create socket");
                socket_in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                Log.d("Stream creaed","Stream creaed");
                Log.d("readLind ", "readLind");
                data = socket_in.readLine();
                if (data.equals("A")) {
                    dataInput="1";
                } else if(data.equals("B")){
                    dataInput="2";
                } else if(data.equals("C")){
                    dataInput="3";
                }
                Log.d("catch : ", "" + data);
                socket.close();
                socket_in.close();
                try { Thread.sleep(1000);} catch (Exception e){}

            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    };
}
