function createTimeDrivenTriggers() {
  ScriptApp.newTrigger('collect_data')
      .timeBased()
      .atHour(20)
      .nearMinute(00)
      .everyDays(1)
      .create();
}
