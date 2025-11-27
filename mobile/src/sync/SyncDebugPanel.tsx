import React from "react";
import { View, Text, Button } from "react-native";

export const SyncDebugPanel = () => {
  const handlePull = () => {
    // Placeholder for calling backend MobileSyncService.pull_changes
  };

  const handlePush = () => {
    // Placeholder for calling backend MobileSyncService.push_changes
  };

  return (
    <View style={{ marginTop: 16 }}>
      <Text>Sync placeholder – no real connectivity in Phase 1 skeleton.</Text>
      <View style={{ flexDirection: "row", marginTop: 8 }}>
        <Button title="Pull Changes" onPress={handlePull} />
        <View style={{ width: 8 }} />
        <Button title="Push Changes" onPress={handlePush} />
      </View>
    </View>
  );
};
