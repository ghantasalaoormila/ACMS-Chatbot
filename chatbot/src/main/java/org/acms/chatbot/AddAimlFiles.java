package org.acms.chatbot;

import java.io.File;

import org.alicebot.ab.Bot;
import org.alicebot.ab.MagicBooleans;

public class AddAimlFiles {

	private static final boolean TRACE_MODE = false;
	static String botName = "super";

	public static void main(String[] args) {
		try {

			String resourcesPath = getResourcesPath();
			System.out.println(resourcesPath);
			MagicBooleans.trace_mode = TRACE_MODE;
			Bot bot = new Bot("jarvis", resourcesPath);
			
			bot.writeAIMLFiles();


		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	private static String getResourcesPath() {
		String path = "/home/oormila/eclipse-workspace/chatbot";
		String resourcesPath = path + File.separator + "src" + File.separator + "main" + File.separator + "resources";
		return resourcesPath;
	}

}
