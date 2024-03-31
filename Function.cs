using System;
using System.IO;
using System.Net.Http;
using System.Text;
using Amazon.Lambda.Core;
using Newtonsoft.Json;

[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

public class Function
{
    public string FunctionHandler(string input, ILambdaContext context)
    {
        dynamic json = JsonConvert.DeserializeObject<dynamic>(input);
        string payload = $"{{\"text\":\"Issue Created: {json.issue.html_url}\"}}";

        using (var client = new HttpClient())
        {
            var content = new StringContent(payload, Encoding.UTF8, "application/json");
            var response = client.PostAsync(Environment.GetEnvironmentVariable("SLACK_URL"), content).Result;

            using (var reader = new StreamReader(response.Content.ReadAsStream()))
            {
                return reader.ReadToEnd
            }
        }
    }
}
