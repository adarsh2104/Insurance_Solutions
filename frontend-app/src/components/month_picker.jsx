import React, { useState } from "react";
import ReactDOM from "react-dom";
import ReactMonthPicker from "react-month-picker";
import "react-month-picker/css/month-picker.css";

const MonthPicker = ({ range }) => {
  const [isVisible, setVisibility] = useState(false);
  const [monthYear, setMonthYear] = useState({});

  const showMonthPicker = event => {
    setVisibility(true);
    event.preventDefault();
  };

  const handleOnDismiss = () => {
    setVisibility(false);
  };

  const handleOnChange = (year, month) => {
    setMonthYear({ year, month });
    setVisibility(false);
  };

  const getMonthValue = () => {
    const month = monthYear && monthYear.month ? monthYear.month : 0;
    const year = monthYear && monthYear.year ? monthYear.year : 0;

    return month && year ? `${month}-${year}` : "Select Month";
  };

  return (
    <div className="MonthYearPicker">
      <button onClick={showMonthPicker}>{getMonthValue()}</button>

      <ReactMonthPicker
        show={isVisible}
        lang={[
          "Jan",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "Jun",
          "Jul",
          "Aug",
          "Sep",
          "Oct",
          "Nov",
          "Dec"
        ]}
        years={range}
        value={monthYear}
        onChange={handleOnChange}
        onDismiss={handleOnDismiss}
      />
    </div>
  );
};

function CustomMonthPicker() {
  const range = {
    min: { year: 2020, month: 3 },
    max: { year: 2025, month: 2 }
  };

  return (
    <div className="App">
      <MonthPicker range={range} />
    </div>
  );
}

export default CustomMonthPicker