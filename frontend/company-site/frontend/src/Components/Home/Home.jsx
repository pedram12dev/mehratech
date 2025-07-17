import React, { useEffect, useState } from "react";
import "./Home.css";

const Home = () => {
  const [projects, setProjects] = useState([]);
  const [members, setMembers] = useState([]);
  const [loadingProjects, setLoadingProjects] = useState(true);
  const [loadingMembers, setLoadingMembers] = useState(true);
  const [errorProjects, setErrorProjects] = useState(null);
  const [errorMembers, setErrorMembers] = useState(null);

  const projectsApi = "http://127.0.0.1:5000/api/projects";
  const membersApi = "http://127.0.0.1:5000/api/members";

  useEffect(() => {
    fetch(projectsApi)
      .then((res) => {
        if (!res.ok) throw new Error("خطا در دریافت پروژه‌ها");
        return res.json();
      })
      .then((data) => setProjects(data))
      .catch((err) => setErrorProjects(err.message))
      .finally(() => setLoadingProjects(false));

    fetch(membersApi)
      .then((res) => {
        if (!res.ok) throw new Error("خطا در دریافت اعضا");
        return res.json();
      })
      .then((data) => setMembers(data))
      .catch((err) => setErrorMembers(err.message))
      .finally(() => setLoadingMembers(false));
  }, []);

  const chunkArray = (arr, size) => {
    const chunks = [];
    for (let i = 0; i < arr.length; i += size) {
      chunks.push(arr.slice(i, i + size));
    }
    return chunks;
  };

  return (
    <div className="full-container">
      <div className="header-container">
        <header>
          <h2>خوش آمدید به صفحه اصلی</h2>
        </header>
      </div>

      <div className="description-container">
        <p className="desciption-paragraph">
          لورم ایپسوم یا متن ساختگی به متنی گفته می‌شود که برای پر کردن فضا و نمایش ظاهر کلی طرح به کار می‌رود...
        </p>
      </div>

      <div className="projects-container">
        <h2>پروژه‌ها</h2>
        {loadingProjects && <p>در حال بارگذاری پروژه‌ها...</p>}
        {errorProjects && <p style={{ color: "red" }}>{errorProjects}</p>}
        {!loadingProjects && !errorProjects && chunkArray(projects, 3).map((row, i) => (
          <div key={i} className="projects-row">
            {row.map((project) => (
              <div key={project.id} className="project-card">
                <img src={project.image} alt={project.title} />
                <h3>{project.title}</h3>
              </div>
            ))}
          </div>
        ))}
      </div>

      <div className="members-container">
        <h2>اعضا</h2>
        {loadingMembers && <p>در حال بارگذاری اعضا...</p>}
        {errorMembers && <p style={{ color: "red" }}>{errorMembers}</p>}
        {!loadingMembers && !errorMembers && chunkArray(members, 3).map((row, i) => (
          <div key={i} className="members-row">
            {row.map((member) => (
              <div key={member.id} className="member-card">
                <img src={member.photo} alt={member.name} />
                <h3>{member.name}</h3>
                <p>{member.specialty}</p>
              </div>
            ))}
          </div>
        ))}
      </div>

      <div className="footer-container">
        <footer>
        </footer>
      </div>
    </div>
  );
};

export default Home;
