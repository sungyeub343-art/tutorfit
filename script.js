const programs = {
  elementary: {
    focus: "개념의 뿌리부터 탄탄하게",
    title: "수학적 호기심과 올바른 학습 습관",
    items: ["교과 개념을 그림과 생활 사례로 이해", "연산 정확도와 문장제 해석력 강화", "학생 스스로 설명하는 풀이 훈련"]
  },
  middle: {
    focus: "개념을 문제 해결력으로",
    title: "내신과 고등 수학을 잇는 단단한 기본기",
    items: ["학교별 진도에 맞춘 개념과 유형 학습", "취약 단원 분석과 반복 오답 관리", "서술형 풀이 과정과 시험 시간 관리"]
  },
  high: {
    focus: "목표 등급에 맞춘 전략적 학습",
    title: "개념 연결부터 실전 적용까지",
    items: ["내신과 모의고사 결과 기반 취약점 진단", "고난도 문제의 조건 해석과 발상 훈련", "개인별 시험 전략과 주간 학습량 관리"]
  }
};

const menuButton = document.querySelector(".menu-button");
const navigation = document.querySelector(".main-nav");

menuButton.addEventListener("click", () => {
  const isOpen = navigation.classList.toggle("is-open");
  menuButton.setAttribute("aria-expanded", String(isOpen));
  menuButton.setAttribute("aria-label", isOpen ? "메뉴 닫기" : "메뉴 열기");
});

navigation.addEventListener("click", () => {
  navigation.classList.remove("is-open");
  menuButton.setAttribute("aria-expanded", "false");
});

document.querySelectorAll(".program-tab").forEach((tab) => {
  tab.addEventListener("click", () => {
    const selected = programs[tab.dataset.program];
    document.querySelectorAll(".program-tab").forEach((item) => {
      const isSelected = item === tab;
      item.classList.toggle("is-active", isSelected);
      item.setAttribute("aria-selected", String(isSelected));
    });

    const panel = document.querySelector(".program-panel");
    panel.querySelector(".program-focus").textContent = selected.focus;
    panel.querySelector("h3").textContent = selected.title;
    panel.querySelector("ul").innerHTML = selected.items.map((item) => `<li>${item}</li>`).join("");
  });
});

const consultForm = document.querySelector(".consult-form");
consultForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const status = consultForm.querySelector(".form-status");
  const submitButton = consultForm.querySelector('button[type="submit"]');

  if (!consultForm.checkValidity()) {
    consultForm.reportValidity();
    status.textContent = "필수 항목을 확인해 주세요.";
    return;
  }

  submitButton.disabled = true;
  submitButton.textContent = "전송 중...";
  status.textContent = "";

  try {
    const response = await fetch(consultForm.action, {
      method: "POST",
      body: new FormData(consultForm),
      headers: { Accept: "application/json" }
    });

    if (!response.ok) throw new Error("Consultation submission failed");

    consultForm.reset();
    status.textContent = "무료 상담이 신청되었습니다. 확인 후 연락드리겠습니다.";
  } catch {
    status.textContent = "전송하지 못했습니다. 잠시 후 다시 시도해 주세요.";
  } finally {
    submitButton.disabled = false;
    submitButton.textContent = "무료 상담 신청하기";
  }
});