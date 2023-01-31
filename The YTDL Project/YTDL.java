import javax.swing.JOptionPane;
import java.awt.AWTException;
import java.awt.event.KeyEvent;
import java.awt.Robot;
import java.io.*;
import java.awt.datatransfer.*;
import java.awt.*;

public class YTDL{
    //Wow I do not like Java
    public static void main(String args[]) throws IOException, AWTException, InterruptedException{
        String linkage;
        // Gather Link
        linkage= JOptionPane.showInputDialog("Enter Your Link here!");
        
        //Checking you copied in the right thing
        int response = JOptionPane.showConfirmDialog(null, "The link you have is " + linkage + " is this correct?", "Confirmation", JOptionPane.YES_NO_OPTION);
        
        //If Yes, do all of this
        if (response == JOptionPane.YES_OPTION){
            //Let's you know we're starting
            JOptionPane.showMessageDialog(null, "You got it! Let's get this open!");
            //Open Program
            String command = "C:\\Program Files\\ConEmu\\ConEmu64.exe";
            Runtime run = Runtime.getRuntime();   
            run.exec(command);
            
            //Honestly still don't know what this does.
            try{   
            //delay 1.5s  
            Thread.sleep(1500);   
            }   
            catch (InterruptedException e){ 
                e.printStackTrace();
            } 
            
            //Having to manually type all of this out is awful
            //Navigating to my D: Drive
            Robot keysOne = new Robot();
            keysOne.keyPress(KeyEvent.VK_C);
            Thread.sleep(200);
            keysOne.keyPress(KeyEvent.VK_D);
            Thread.sleep(200);
            keysOne.keyPress(KeyEvent.VK_SPACE);
            Thread.sleep(200);
            keysOne.keyPress(KeyEvent.VK_SHIFT);
            keysOne.keyPress(KeyEvent.VK_D);
            keysOne.keyRelease(KeyEvent.VK_SHIFT);
            Thread.sleep(200);
            keysOne.keyPress(KeyEvent.VK_SHIFT);
            keysOne.keyPress( KeyEvent.VK_SEMICOLON);
            keysOne.keyRelease(KeyEvent.VK_SHIFT);
            Thread.sleep(200);
            keysOne.keyPress(KeyEvent.VK_Y);
            Thread.sleep(200);
            keysOne.keyPress(KeyEvent.VK_O);
            Thread.sleep(200);
            keysOne.keyPress(KeyEvent.VK_U);
            Thread.sleep(200);
            keysOne.keyPress(KeyEvent.VK_T);
            Thread.sleep(200);
            keysOne.keyPress(KeyEvent.VK_U);
            Thread.sleep(200);
            keysOne.keyPress(KeyEvent.VK_B);
            Thread.sleep(200);
            keysOne.keyPress(KeyEvent.VK_E);
            Thread.sleep(200);
            keysOne.keyPress(KeyEvent.VK_MINUS);
            Thread.sleep(200);
            keysOne.keyPress(KeyEvent.VK_D);
            Thread.sleep(200);
            keysOne.keyPress(KeyEvent.VK_L);
            Thread.sleep(2000);
            keysOne.keyPress(KeyEvent.VK_ENTER);
            keysOne.keyRelease(KeyEvent.VK_ENTER);
            
            //Pause so keystrokes don't overlap
            Thread.sleep(1000);

            //Getting to the D:
            Robot keysTwo = new Robot();
            keysTwo.keyPress(KeyEvent.VK_SHIFT);
            keysTwo.keyPress(KeyEvent.VK_D);
            Thread.sleep(200);
            keysTwo.keyPress(KeyEvent.VK_SHIFT);
            keysTwo.keyPress( KeyEvent.VK_SEMICOLON);
            keysTwo.keyRelease(KeyEvent.VK_SHIFT);
            Thread.sleep(1000);
            keysTwo.keyPress(KeyEvent.VK_ENTER);
            Thread.sleep(500);

            //Part 3: Manually passing through the codec preference + link to clipboard
            String codecs = "yt-dlp -f bestaudio[ext=m4a]+bestvideo[ext=mp4] " + linkage;
            StringSelection stringSelection = new StringSelection(codecs);
            Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
            clipboard.setContents(stringSelection, stringSelection);

            //Use the robot to paste that in.
            Robot pasting = new Robot();
            pasting.keyPress(KeyEvent.VK_CONTROL);
            pasting.keyPress(KeyEvent.VK_V);
            pasting.keyRelease(KeyEvent.VK_V);
            pasting.keyRelease(KeyEvent.VK_CONTROL);
            Thread.sleep(500);
            pasting.keyPress(KeyEvent.VK_ENTER);
            pasting.keyRelease(KeyEvent.VK_ENTER);

            //I probably could make this a confirmation dialog to have it loop around, but I'm too frustrated to attempt it.
            Thread.sleep(5000);
            JOptionPane.showMessageDialog(null, "I'm Done Good Bye!");
            System.exit(0);
           
        }
        //If you say no or cancel, close it down.
        else { 
            JOptionPane.showMessageDialog(null, "Check your links and try again!");
            System.out.println("Closing down...");
            System.exit(0);
        }
    }
}