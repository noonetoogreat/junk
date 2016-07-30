import java.util.*;
import java.io.*;
import java.net.*;

class Responder{
	public static void main(String[] args) throws Exception {
		ServerSocket soc = new ServerSocket(8719);
		String nonce2 = "222222"
		BufferedReader infromIni = new BufferedReader (new InputstreamReader(in.getInputStream()));
		
		try{
			
			Socket in = soc.accept();
			DataOutputStream Output = new DataOutputStream(sock.getOutputStream());
			
			
			String h1 = infromIni.readLine();		//Receive First handshake
			System.out.println("Handshake (in): " + h1);
			
			String nonce1 = h1.substring(0,6);
			
			String h2=nonce1+nonce2;
			Output.writeBytes(h2);				//Send Second Handshake
			System.out.println("Handshake (out): " + h2);

			String h3 = infromIni.readLine();		//Receive Third handshake
			System.out.println("Handshake (in): " + h3);
			
			String h4 = infromIni.readLine();		//Receive Fourth handshake
			System.out.println("Handshake (in): " + h4);

			sock.close();
		}catch(Exception e)
		{
			System.err.println(e);
		}			
	}
}

