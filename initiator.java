import java.util.*;
import java.io.*;
import java.net.*;

class Initiator{
	public static void main(String[] args) throws Exception{
		
		InetAddress address = InetAddress.getLocalHost();
		String nonce1 = "111111"
		try{
			Socket sock = new Socket ("localhost",8719);
			BufferedReader infromResp = new BufferedReader (new InputstreamReader(in.getInputStream()));
			
			DataOutputStream Output = new DataOutputStream(sock.getOutputStream()); 
			
			String h1 = nonce1+address.toString();
			Output.writeBytes(h1);		// Send First handshake
			System.out.println("Handshake: " + h1);
			
			String h2 = infromResp.readLine();	//Receive Second Handshake
			System.out.println("Handshake: " + h2);		
			
			String nonce2 = h2.substring(6,12);

			String h3 = nonce2;
			Output.writeBytes(h3);		// Send Third handshake
			System.out.println("Handshake: " + h3);

			String h4 = 
			Output.writeBytes(h4);		// Send Fourth handshake
			System.out.println("Handshake: " + h4);

			sock.close();
		}catch(Exception e)
		{	System.err.println(e);
		}
	}
}

