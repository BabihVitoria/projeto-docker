import java.io.*;  
    import java.net.*; 
    public class script {
    public static void main(String[] args) {  

    try{      
    Socket soc=new Socket("172.17.0.2",5000);  //criar conexao com o servidor
    DataOutputStream dout=new DataOutputStream(soc.getOutputStream());   //criar buffer de scrita
    dout.writeUTF("ola mundo"); //escreve dados no socker
    dout.flush();//limpa o buffer de escrita
    dout.close();  //fecha o buffer de escrita
    soc.close();//fecha aconexao com o servidor
    }catch(Exception e){
        e.printStackTrace();
	System.out.println("Deu erro: " + e.getMessage());
}  
    }  
}