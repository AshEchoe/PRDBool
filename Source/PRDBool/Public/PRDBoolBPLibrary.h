// Copyright SkyWing All Rights Reserved.

#pragma once

#include "Kismet/BlueprintFunctionLibrary.h"
#include "PRDBoolBPLibrary.generated.h"

UCLASS()
class UPRDBoolBPLibrary : public UBlueprintFunctionLibrary
{
	GENERATED_UCLASS_BODY()

	//计算伪随机分布布尔值
	UFUNCTION(BlueprintCallable, meta = (DisplayName = "Calculate Pseudo Random Bool", ToolTip = "Calculates a random boolean value based on the given probability and count.\nMake the random results closer to the average case.\nInput Parameters\nProbability: The probability that requires pseudo random distribution calculation., which should be in the range of 0 to 1.\nCount : The cumulative count for pseudo random distribution calculation. Changes in the Count value will affect the probability of IsSuccess returning true.\nOutput Parameters\nIsSuccess : The random Boolean value returned based on Probability and Count.\nNewCount : The cumulative count after the calculation is completed.When IsCuccess returns true, NewCount returns 0; when IsSuccess returns false, NewCount returns Count + 1.", Category = "Math|Random"))
	static void RandomBoolWithPRD(UPARAM(DisplayName = "Probability") float Probability,UPARAM(DisplayName = "Count") int32 Count,UPARAM(DisplayName = "IsSuccess") bool& IsSuccess,UPARAM(DisplayName = "NewCount") int32& NewCount);

	//获取伪随机分布概率增量
	UFUNCTION(Blueprintpure, meta = (ReturnDisplayName = "ProbabilityIncrement",DisplayName = "Get Pseudo Random Probability Increment", ToolTip = "The constant probability increment corresponding to Probability.", Category = "Math|Random"))
	static float GetProbabilityIncrement(UPARAM(DisplayName = "Probability") float Probability);
};
