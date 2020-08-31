# ChangeAttributeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the attribute to be changed. Silently ignored if the ID is provided as path parameter of the request. | 
**value** | [**object**](.md) | The value of this attribute. Expected type of the value depends on the type of the attribute.&lt;br/&gt;Following list presents type of the value depending on the kind of the attribute&lt;br/&gt;&lt;ul&gt;&lt;br/&gt;&lt;li&gt; kind: Numeric               -&gt; value type: number or string&lt;br/&gt;&lt;li&gt; kind: Script                -&gt; value type: string&lt;br/&gt;&lt;li&gt; kind: Single Value List     -&gt; value type: string&lt;br/&gt;&lt;li&gt; kind: Date                  -&gt; value type: number or string&lt;br/&gt;&lt;li&gt; kind: String                -&gt; value type: string&lt;br/&gt;&lt;li&gt; kind: Boolean               -&gt; value type: boolean or string&lt;br/&gt;&lt;li&gt; kind: Multi Value List      -&gt; value type: array of strings&lt;br/&gt;&lt;/ul&gt; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


