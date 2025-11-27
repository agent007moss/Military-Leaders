import React from "react";
import { View, Text } from "react-native";
import { SyncDebugPanel } from "./sync/SyncDebugPanel";

export const App = () => {
  return (
    <View style={{ flex: 1, padding: 16 }}>
      <Text style={{ fontSize: 18, fontWeight: "600", marginBottom: 8 }}>
        Military Leaders Tool – Mobile Skeleton
      </Text>
      <SyncDebugPanel />
    </View>
  );
};
