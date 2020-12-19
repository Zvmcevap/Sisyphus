$(document).ready(function () {
  for (i = 1; i <= 31; i++) {
    $(".month").append(
      ` <div class="d-flex flex-column daysofmonth">
            <label for="${i}">
              ${i}
            </label>
            <input
              name="${i}"
              id="${i}"
              class="form-control-sm"
              type="checkbox"
            />
          </div>`
    );
  }
  // Setting Date and Time in the form
  class DateTimeClass {
    constructor(date) {
      this.date = date;
    }
    getDateStr() {
      return this.date.toISOString().slice(0, 10);
    }
    getTimeStr() {
      return this.date.toISOString().slice(11, 16);
    }
    addHourTimeStr() {
      let time = new Date(this.date.getTime() + 3600000);
      return time.toISOString().slice(11, 16);
    }
    addDayDateStr() {
      let day = new Date(this.date.getTime() + 86400000);
      return day.toISOString().slice(0, 10);
    }
    isSmallerDate(insertedDate) {
      if (this.date.getTime() <= insertedDate.gettime()) {
        return false;
      } else {
        return true;
      }
    }
  }

  function fromDateInputtoObj(wantFrom) {
    dateId = wantFrom ? "#from-date" : "#to-date";
    timeId = wantFrom ? "#from-time" : "#to-time";
    console.log($(timeId).val());
    dateStrs = $(dateId).val().split("-");
    timeStrs = $(timeId).val().split(":");
    console.log(timeStrs);

    return new Date(
      Number(dateStrs[0]),
      Number(dateStrs[1]) - 1,
      Number(dateStrs[2]),
      Number(timeStrs[0]),
      Number(timeStrs[1]),
      0,
      0
    );
  }

  let now = new DateTimeClass(new Date());
  $("#from-date").attr("value", now.getDateStr());
  $("#from-time").attr("value", now.getTimeStr());

  $("#to-date").attr("value", now.getDateStr());
  $("#to-time").attr("value", now.addHourTimeStr());

  $("#from-date").change(function () {
    console.log($("#from-date").val());
  });
  let wantFrom = true;
  fromDate = fromDateInputtoObj(wantFrom);
  console.log(fromDate.toISOString());

  /*
  // Using the whole day parameter
  function isWholeDay(bol) {
    if (bol) {
      $("#from-time").val("00:00").prop("disabled", true);
      $("#to-time").val("00:00").prop("disabled", true);
      $("#to-date").val(nextDayStr);
    } else {
      $("#from-time").val(nowTimeStr).prop("disabled", false);
      $("#to-time").val(thenTimeStr).prop("disabled", false);
      $("#to-date").val(nowDateStr);
    }
  }
*/
  let wholeDayCheck = $("#whole-day-check").prop("checked");

  $("#whole-day-check").click(function () {
    wholeDayCheck = $("#whole-day-check").prop("checked");
    isWholeDay(wholeDayCheck);
  });
});
