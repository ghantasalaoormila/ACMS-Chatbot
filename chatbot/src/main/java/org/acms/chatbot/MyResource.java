package org.acms.chatbot;

import javax.ws.rs.Consumes;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import org.json.JSONException;
import org.json.JSONObject;

/**
 * Root resource (exposed at "myresource" path)
 */
@Path("myresource")
public class MyResource {
    /**
     * Method handling HTTP GET requests. The returned object will be sent
     * to the client as "text/plain" media type.
     *
     * @return String that will be returned as a text/plain response.
     * @throws JSONException 
     */
	
	 @POST
	 @Path("/getIt")
	 @Consumes("application/json")
	 @Produces(MediaType.APPLICATION_JSON)
	 public String getIt() throws JSONException {
		 JSONObject reply = new JSONObject();
	     reply.put("reply","Got it!");
	     return reply.toString();
	 }
	
    @POST
    @Path("/getResponse")
    @Consumes("application/json")
    @Produces(MediaType.APPLICATION_JSON)
    public String getResponse(String message) throws JSONException {
    	JSONObject user_obj = new JSONObject(message);
    	JSONObject reply = new JSONObject();
    	reply.put("reply","Can't connect right now");
    	Chatbot chatbot = Chatbot.getInstance();
    	String r = chatbot.getResponse(user_obj.getString("q"));
    	reply.put("reply",r);
		return reply.toString();
    }
}
