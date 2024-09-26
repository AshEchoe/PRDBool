// Copyright SkyWing All Rights Reserved.

#pragma once

#include "Kismet/BlueprintFunctionLibrary.h"
#include "PRDBoolBPLibrary.generated.h"

UCLASS()
class UPRDBoolBPLibrary : public UBlueprintFunctionLibrary
{
	GENERATED_UCLASS_BODY()

	UFUNCTION(BlueprintCallable, meta = (DisplayName = "Calculate Pseudo Random Bool", ToolTip = "Calculates a pseudo-random boolean value based on the given probability and count, returning a random result.\nMake the random results closer to the average case.\nFor example, To avoid situations where, with a 50% critical hit rate, there are 10 consecutive critical hits or 10 consecutive non-critical hits, the goal is to make the critical hit closer to the average rate.\nInput Parameters\nProbability: The probability of selecting true (success)in a pseudo - random manner, which should be in the range of 0 to 1.\nCount : The number of iterations for the random calculation, determining the sample size for the computation.\nOutput Parameters\nIsSuccess : Indicates whether the final computation was successful.\nNewCount : Represents the count after the computation is completed.When IsCuccess returns true, NewCount returns 0; when IsSuccess returns false, NewCount returns Count + 1.", Category = "Math|Random"))
	static void RandomBoolWithPRD(UPARAM(DisplayName = "Probability") float Probability,UPARAM(DisplayName = "Count") int32 Count,UPARAM(DisplayName = "IsSuccess") bool& IsSuccess,UPARAM(DisplayName = "NewCount") int32& NewCount);
};
