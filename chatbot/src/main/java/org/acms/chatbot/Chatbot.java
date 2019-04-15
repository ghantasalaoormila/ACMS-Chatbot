package org.acms.chatbot;

import java.io.File;
import org.alicebot.ab.Bot;
import org.alicebot.ab.Chat;
import org.alicebot.ab.History;
import org.alicebot.ab.MagicBooleans;

import com.google.cloud.translate.Detection;
import com.google.cloud.translate.Translate;
import com.google.cloud.translate.Translate.TranslateOption;
import com.google.cloud.translate.TranslateOptions;
import com.google.cloud.translate.Translation;


public class Chatbot {
	private static final boolean TRACE_MODE = false;
	private static Chatbot instance = null;
	static String botName = "super";
	Chat chatSession;
	Bot bot;
	String textLine;
	private Chatbot() {
		textLine = "Hi";
		String resourcesPath = getResourcesPath();
		System.out.println(resourcesPath);
		MagicBooleans.trace_mode = TRACE_MODE;
		bot = new Bot("jarvis", resourcesPath);
		chatSession = new Chat(bot);
		bot.brain.nodeStats();
	}
	
	public static synchronized Chatbot getInstance() {
		if(instance==null) instance = new Chatbot();
		return instance;
	}
	
	@SuppressWarnings({ "rawtypes" })
	public String getResponse(String str) {
		textLine = str;
		Translate translate = TranslateOptions.getDefaultInstance().getService();
		Detection detection = translate.detect(textLine);
		String detectedLanguage = detection.getLanguage();
		if(!detectedLanguage.equals("en")) {
			Translation translation =
			        translate.translate(
			            textLine,
			            TranslateOption.sourceLanguage(detectedLanguage),
			            TranslateOption.targetLanguage("en"));
			textLine = translation.getTranslatedText();
		}
		String reply = "";
		try {
			

			if ((textLine == null) || (textLine.length() < 1)) {
				return "Ummm...";
			} else {
				String request = textLine;
				if (MagicBooleans.trace_mode)
					System.out.println("STATE=" + request + ":THAT=" + ((History) chatSession.thatHistory.get(0)).get(0) + ":TOPIC=" + chatSession.predicates.get("topic"));
				String response = chatSession.multisentenceRespond(request);
				while (response.contains("&lt;"))
					response = response.replace("&lt;", "<");
				while (response.contains("&gt;"))
					response = response.replace("&gt;", ">");
				System.out.println("Robot : " + response);
				reply = response;
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		if(!detectedLanguage.equals("en")) {
			Translation translation =
			        translate.translate(
			            reply,
			            TranslateOption.sourceLanguage("en"),
			            TranslateOption.targetLanguage(detectedLanguage));
			reply = translation.getTranslatedText();
		}
		return reply;
	}

	private String getResourcesPath() {
		String path = "/home/oormila/eclipse-workspace/chatbot";
		String resourcesPath = path + File.separator + "src" + File.separator + "main" + File.separator + "resources";
		return resourcesPath;
	}

}
