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
    constructor(fromDate, toDate) {
      this.fromDate = fromDate;
      this.toDate = toDate;
    }
    getFromDateStr(fromBol) {
      if (fromBol) {
        return this.fromDate.toISOString().slice(0, 10);
      } else {
        return this.toDate.toISOString().slice(0, 10);
      }
    }
    getFromTimeStr(fromBol) {
      if (fromBol) {
        return this.fromDate.toISOString().slice(11, 16);
      } else {
        return this.toDate.toISOString().slice(11, 16);
      }
    }
    addHourToDate(fromBol) {
      console.log(this.toDate);
      if (fromBol) {
        this.toDate = new Date(this.fromDate.getTime() + 3600000);
      } else {
        this.fromDate = new Date(this.toDate.getTime() - 3600000);
      }
    }
    addDayToDate(fromBol) {
      console.log(this.toDate);
      if (fromBol) {
        this.toDate = new Date(this.fromDate.getTime() + 86400000);
      } else {
        this.fromDate = new Date(this.toDate.getTime() - 86400000);
      }
    }
    compareFrom(fromBol, wholeDay) {
      if (this.fromDate.getTime() >= this.toDate.getTime()) {
        if (wholeDay) {
          this.addDayToDate(fromBol);
        } else {
          this.addHourToDate(fromBol);
        }
      }
    }
  }

  // Function to get DateTime Class from Input
  function fromDateInputtoObj(wantFrom) {
    dateId = wantFrom ? "#from-date" : "#to-date";
    timeId = wantFrom ? "#from-time" : "#to-time";
    dateStrs = $(dateId).val().split("-");
    timeStrs = $(timeId).val().split(":");

    return new Date(
      Number(dateStrs[0]),
      Number(dateStrs[1]) - 1,
      Number(dateStrs[2]),
      Number(timeStrs[0]) + 1,
      Number(timeStrs[1]),
      0,
      0
    );
  }
  // End of the Function Def
  let wholeDayCheck = $("#whole-day-check").prop("checked");

  let now = new Date();
  now.setTime(now.getTime() - now.getTimezoneOffset() * 60 * 1000);

  const mainDateTimeClass = new DateTimeClass(now, now);
  mainDateTimeClass.compareFrom(true);

  $("#from-date").attr("value", mainDateTimeClass.getFromDateStr(true));
  $("#from-time").attr("value", mainDateTimeClass.getFromTimeStr(true));

  $("#to-date").attr("value", mainDateTimeClass.getFromDateStr(false));
  $("#to-time").attr("value", mainDateTimeClass.getFromTimeStr(false));

  // When the Dates and Times get changed
  $(".fromDateTime").change(function () {
    mainDateTimeClass.fromDate = fromDateInputtoObj(true);
    mainDateTimeClass.compareFrom(true, wholeDayCheck);

    $("#to-date").val(mainDateTimeClass.getFromDateStr(false));
    $("#to-time").val(mainDateTimeClass.getFromTimeStr(false));
  });
  $(".toDateTime").change(function () {
    mainDateTimeClass.toDate = fromDateInputtoObj(false);
    mainDateTimeClass.compareFrom(false, wholeDayCheck);

    $("#from-date").val(mainDateTimeClass.getFromDateStr(true));
    $("#from-time").val(mainDateTimeClass.getFromTimeStr(true));
  });

  // Using the whole day parameter
  function isWholeDay(bol) {
    if (bol) {
      $("#from-time").val("00:00").prop("disabled", true);
      mainDateTimeClass.fromDate = fromDateInputtoObj(true);
      $("#to-time").val("00:00").prop("disabled", true);
      mainDateTimeClass.toDate = fromDateInputtoObj(false);
      mainDateTimeClass.compareFrom(true, bol);
      $("#to-date").val(mainDateTimeClass.getFromDateStr(false));
    } else {
      $("#from-time").prop("disabled", false);
      $("#to-time").prop("disabled", false);
    }
  }

  $("#whole-day-check").click(function () {
    wholeDayCheck = $("#whole-day-check").prop("checked");
    isWholeDay(wholeDayCheck);
  });
});
