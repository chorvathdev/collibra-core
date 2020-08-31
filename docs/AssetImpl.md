# AssetImpl

The list of results.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the represented object (entity). | 
**created_by** | **str** | The id of the user that created this resource. | [optional] 
**created_on** | **int** | The timestamp (in UTC time standard) of the creation of this resource. | [optional] 
**last_modified_by** | **str** | The id of the user who modified this resource the last time. | [optional] 
**last_modified_on** | **int** | The timestamp (in UTC time standard) of the last modification of this resource. | [optional] 
**system** | **bool** | Whether this is a system resource or not. | [optional] 
**resource_type** | **str** | The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]. | 
**name** | **str** | The name of the resource. | [optional] 
**display_name** | **str** | The display name of the asset.  &lt;p&gt;  Please note that \&quot;displayName\&quot; corresponds to the \&quot;Name\&quot; in the UI. | [optional] 
**articulation_score** | **float** | The articulation score for this asset.  &lt;p&gt;  Expresses how well this asset is articulated.  The articulation score is a percentage number ranging from 0 to 100.  The articulation rules can be configured to calculate the articulation score.  Whenever the asset is modified, by changing its attributes or statuses, the articulation score is re-evaluated. | [optional] 
**excluded_from_auto_hyperlinking** | **bool** | Whether this asset is excluded from hyperlinking or not. | [optional] 
**domain** | [**NamedResourceReferenceImpl**](NamedResourceReferenceImpl.md) |  | [optional] 
**type** | [**NamedResourceReferenceImpl**](NamedResourceReferenceImpl.md) |  | [optional] 
**status** | [**NamedResourceReferenceImpl**](NamedResourceReferenceImpl.md) |  | [optional] 
**avg_rating** | **float** | The average rating. | [optional] 
**ratings_count** | **int** | The number of ratings. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


