import React from "react";
import { useNavigate } from "react-router-dom";

const Services = () => {
  const navigate = useNavigate();

  const goToContact = () => {
    navigate("/contact");
  };

  return (
    <div style={{ padding: "20px" , direction: "rtl" }}>
      <h2>خدمات ما</h2>
      <p>در این بخش می‌توانید خدمات ارائه شده توسط شرکت را مشاهده کنید.</p>
      <ul>
        <li>خدمات مشاوره</li>
        <li>توسعه نرم‌افزار</li>
        <li>طراحی وب‌سایت</li>
        <li>پشتیبانی فنی</li>
      </ul>
      <button onClick={goToContact} style={{ marginTop: "20px", padding: "10px 20px", cursor: "pointer" }}>
        تماس با ما برای مشاوره
      </button>
    </div>
  );
};

export default Services;
