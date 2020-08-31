# AddComplexRelationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the new complex relation. Should be unique within all complex relations and assets.&lt;br/&gt;It should have a format of universally unique identifier (UUID) and should not start with &lt;code&gt;00000000-0000-0000-&lt;/code&gt; which is a reserved prefix. | [optional] 
**complex_relation_type_id** | **str** | The ID of the type of the complex relation. | 
**legs** | [**list[ComplexRelationLegRequest]**](ComplexRelationLegRequest.md) |  The list of legs that the new complex relation should contain. | [optional] 
**attributes** | **dict(str, list[AttributeValue])** | The attributes that the new complex relation should contain.&lt;br/&gt;&lt;u&gt;Example:&lt;/u&gt;&lt;br/&gt;attributes : {&lt;br/&gt;&amp;emsp;\&quot;00000000-0000-0000-0000-000000003114\&quot;: [&lt;br/&gt;&amp;emsp;&amp;emsp;{&lt;br/&gt;&amp;emsp;&amp;emsp;&amp;emsp;\&quot;value\&quot;: \&quot;string1\&quot;&lt;br/&gt;&amp;emsp;&amp;emsp;}&lt;br/&gt;&amp;emsp;]&lt;br/&gt;&amp;emsp;\&quot;00000000-0000-0000-0000-000000003115\&quot;: [&lt;br/&gt;&amp;emsp;&amp;emsp;{&lt;br/&gt;&amp;emsp;&amp;emsp;&amp;emsp;\&quot;values\&quot;: [&lt;br/&gt;&amp;emsp;&amp;emsp;&amp;emsp;&amp;emsp;\&quot;string2\&quot;,&lt;br/&gt;&amp;emsp;&amp;emsp;&amp;emsp;&amp;emsp;\&quot;string3\&quot;&lt;br/&gt;&amp;emsp;&amp;emsp;&amp;emsp;]&lt;br/&gt;&amp;emsp;&amp;emsp;}&lt;br/&gt;&amp;emsp;]&lt;br/&gt;} | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


