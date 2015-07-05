﻿using System;
using System.Linq;
using System.Reflection;
using BluffinMuffin.Protocol.DataTypes.Attributes;
using BluffinMuffin.Protocol.Enums;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using Newtonsoft.Json.Linq;

namespace BluffinMuffin.Protocol
{
    /// <summary>
    /// 
    /// </summary>
    public abstract class AbstractCommand
    {
        /// <summary>
        /// Always contains '{CommandName}' to distinguish the command from others."
        /// </summary>
        [JsonProperty(Order = -100)]
        [ExampleValue("{CommandName}")]
        public string CommandName { get { return GetType().Name; } }

        /// <summary>
        /// 
        /// </summary>
        [JsonIgnore]
        public abstract BluffinCommandEnum CommandType { get; }

        /// <summary>
        /// Browsing all Types inheriting "AbstractBluffinCommand", it finds the type named exactly like the "CommandName" attribute in the JSON.
        /// </summary>
        public static AbstractCommand DeserializeCommand(string data)
        {
            JObject jObj = JsonConvert.DeserializeObject<dynamic>(data);
            var commandName = jObj["CommandName"].Value<String>();
            Type commType = Assembly.GetAssembly(typeof(AbstractCommand)).GetTypes().Single(t => t.IsClass && !t.IsAbstract && t.IsSubclassOf(typeof(AbstractCommand)) && t.Name == commandName);
            MethodInfo method = typeof(JsonConvert).GetMethods().First(m => m.Name == "DeserializeObject" && m.IsGenericMethod).MakeGenericMethod(new[] { commType });
            return (AbstractCommand)method.Invoke(null, new object[] { data });
        }

        /// <summary>
        /// 
        /// </summary>
        /// <returns></returns>
        public string Encode()
        {
            return JsonConvert.SerializeObject(this, new StringEnumConverter());
        }
    }
}