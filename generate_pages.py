"""부산 지역·학년별 수학과외 페이지와 sitemap.xml을 생성합니다.

사용법: python generate_pages.py
"""
import json
import re
from datetime import date
from pathlib import Path

SITE = "https://tutorfit.kr"
PHONE = "010-2928-3614"
TEL = "tel:01029283614"
BRAND = "부산 수학과외"
LASTMOD = date.today().isoformat()
ROOT = Path(__file__).resolve().parent

DISTRICTS = {
    "jung-gu": ("중구", [
        ("jungang-dong", "중앙동"), ("donggwang-dong", "동광동"), ("daecheong-dong", "대청동"), ("bosu-dong", "보수동"), ("bupyeong-dong", "부평동"), ("gwangbok-dong", "광복동"), ("nampo-dong", "남포동"), ("yeongju-1-dong", "영주1동"), ("yeongju-2-dong", "영주2동"),
    ]),
    "seo-gu": ("서구", [
        ("dongdaesin-1-dong", "동대신1동"), ("dongdaesin-2-dong", "동대신2동"), ("dongdaesin-3-dong", "동대신3동"), ("seodaesin-1-dong", "서대신1동"), ("seodaesin-3-dong", "서대신3동"), ("seodaesin-4-dong", "서대신4동"), ("bumin-dong", "부민동"), ("ami-dong", "아미동"), ("chojang-dong", "초장동"), ("chungmu-dong", "충무동"), ("nambumin-1-dong", "남부민1동"), ("nambumin-2-dong", "남부민2동"), ("amnam-dong", "암남동"),
    ]),
    "dong-gu": ("동구", [
        ("choryang-1-dong", "초량1동"), ("choryang-2-dong", "초량2동"), ("choryang-3-dong", "초량3동"), ("choryang-6-dong", "초량6동"), ("sujeong-1-dong", "수정1동"), ("sujeong-2-dong", "수정2동"), ("sujeong-4-dong", "수정4동"), ("sujeong-5-dong", "수정5동"), ("jwacheon-dong", "좌천동"), ("beomil-1-dong", "범일1동"), ("beomil-2-dong", "범일2동"), ("beomil-5-dong", "범일5동"),
    ]),
    "yeongdo-gu": ("영도구", [
        ("namhang-dong", "남항동"), ("yeongseon-1-dong", "영선1동"), ("yeongseon-2-dong", "영선2동"), ("sinseon-dong", "신선동"), ("bongnae-1-dong", "봉래1동"), ("bongnae-2-dong", "봉래2동"), ("cheonghak-1-dong", "청학1동"), ("cheonghak-2-dong", "청학2동"), ("dongsam-1-dong", "동삼1동"), ("dongsam-2-dong", "동삼2동"), ("dongsam-3-dong", "동삼3동"),
    ]),
    "busanjin-gu": ("부산진구", [
        ("bujeon-1-dong", "부전1동"), ("bujeon-2-dong", "부전2동"), ("yeonji-dong", "연지동"), ("choeup-dong", "초읍동"), ("yangjeong-1-dong", "양정1동"), ("yangjeong-2-dong", "양정2동"), ("jeonpo-1-dong", "전포1동"), ("jeonpo-2-dong", "전포2동"), ("buam-1-dong", "부암1동"), ("buam-3-dong", "부암3동"), ("danggam-1-dong", "당감1동"), ("danggam-2-dong", "당감2동"), ("danggam-4-dong", "당감4동"), ("gaya-1-dong", "가야1동"), ("gaya-2-dong", "가야2동"), ("gaegeum-1-dong", "개금1동"), ("gaegeum-2-dong", "개금2동"), ("gaegeum-3-dong", "개금3동"), ("beomcheon-1-dong", "범천1동"), ("beomcheon-2-dong", "범천2동"),
    ]),
    "dongnae-gu": ("동래구", [
        ("sumin-dong", "수민동"), ("boksan-dong", "복산동"), ("myeongnyun-dong", "명륜동"), ("oncheon-1-dong", "온천1동"), ("oncheon-2-dong", "온천2동"), ("oncheon-3-dong", "온천3동"), ("sajik-1-dong", "사직1동"), ("sajik-2-dong", "사직2동"), ("sajik-3-dong", "사직3동"), ("anrak-1-dong", "안락1동"), ("anrak-2-dong", "안락2동"), ("myeongjang-1-dong", "명장1동"), ("myeongjang-2-dong", "명장2동"),
    ]),
    "nam-gu": ("남구", [
        ("daeyeon-1-dong", "대연1동"), ("daeyeon-3-dong", "대연3동"), ("daeyeon-4-dong", "대연4동"), ("daeyeon-5-dong", "대연5동"), ("daeyeon-6-dong", "대연6동"), ("yongho-1-dong", "용호1동"), ("yongho-2-dong", "용호2동"), ("yongho-3-dong", "용호3동"), ("yongho-4-dong", "용호4동"), ("yongdang-dong", "용당동"), ("gamman-1-dong", "감만1동"), ("gamman-2-dong", "감만2동"), ("uam-dong", "우암동"), ("munhyeon-1-dong", "문현1동"), ("munhyeon-2-dong", "문현2동"), ("munhyeon-3-dong", "문현3동"), ("munhyeon-4-dong", "문현4동"),
    ]),
    "buk-gu": ("북구", [
        ("gupo-1-dong", "구포1동"), ("gupo-2-dong", "구포2동"), ("gupo-3-dong", "구포3동"), ("geumgok-dong", "금곡동"), ("hwamyeong-1-dong", "화명1동"), ("hwamyeong-2-dong", "화명2동"), ("hwamyeong-3-dong", "화명3동"), ("deokcheon-1-dong", "덕천1동"), ("deokcheon-2-dong", "덕천2동"), ("deokcheon-3-dong", "덕천3동"), ("mandeok-1-dong", "만덕1동"), ("mandeok-2-dong", "만덕2동"), ("mandeok-3-dong", "만덕3동"),
    ]),
    "haeundae-gu": ("해운대구", [
        ("u-1-dong", "우1동"), ("u-2-dong", "우2동"), ("u-3-dong", "우3동"), ("jung-1-dong", "중1동"), ("jung-2-dong", "중2동"), ("jwa-1-dong", "좌1동"), ("jwa-2-dong", "좌2동"), ("jwa-3-dong", "좌3동"), ("jwa-4-dong", "좌4동"), ("songjeong-dong", "송정동"), ("bansong-1-dong", "반송1동"), ("bansong-2-dong", "반송2동"), ("banyeo-1-dong", "반여1동"), ("banyeo-2-dong", "반여2동"), ("banyeo-3-dong", "반여3동"), ("banyeo-4-dong", "반여4동"), ("jaesong-1-dong", "재송1동"), ("jaesong-2-dong", "재송2동"),
    ]),
    "saha-gu": ("사하구", [
        ("goejeong-1-dong", "괴정1동"), ("goejeong-2-dong", "괴정2동"), ("goejeong-3-dong", "괴정3동"), ("goejeong-4-dong", "괴정4동"), ("dangni-dong", "당리동"), ("hadan-1-dong", "하단1동"), ("hadan-2-dong", "하단2동"), ("sinpyeong-1-dong", "신평1동"), ("sinpyeong-2-dong", "신평2동"), ("jangnim-1-dong", "장림1동"), ("jangnim-2-dong", "장림2동"), ("dadae-1-dong", "다대1동"), ("dadae-2-dong", "다대2동"), ("gupyeong-dong", "구평동"), ("gamcheon-1-dong", "감천1동"), ("gamcheon-2-dong", "감천2동"),
    ]),
    "geumjeong-gu": ("금정구", [
        ("seo-1-dong", "서1동"), ("seo-2-dong", "서2동"), ("seo-3-dong", "서3동"), ("geumsa-hoedong-dong", "금사회동동"), ("bugok-1-dong", "부곡1동"), ("bugok-2-dong", "부곡2동"), ("bugok-3-dong", "부곡3동"), ("bugok-4-dong", "부곡4동"), ("jangjeon-1-dong", "장전1동"), ("jangjeon-2-dong", "장전2동"), ("seondugu-dong", "선두구동"), ("cheongnyong-nopo-dong", "청룡노포동"), ("namsan-dong", "남산동"), ("guseo-1-dong", "구서1동"), ("guseo-2-dong", "구서2동"), ("geumseong-dong", "금성동"),
    ]),
    "gangseo-gu": ("강서구", [
        ("daejeo-1-dong", "대저1동"), ("daejeo-2-dong", "대저2동"), ("gangdong-dong", "강동동"), ("myeongji-1-dong", "명지1동"), ("myeongji-2-dong", "명지2동"), ("garak-dong", "가락동"), ("noksan-dong", "녹산동"), ("gadeokdo-dong", "가덕도동"), ("sinho-dong", "신호동"),
    ]),
    "yeonje-gu": ("연제구", [
        ("geoje-1-dong", "거제1동"), ("geoje-2-dong", "거제2동"), ("geoje-3-dong", "거제3동"), ("geoje-4-dong", "거제4동"), ("yeonsan-1-dong", "연산1동"), ("yeonsan-2-dong", "연산2동"), ("yeonsan-3-dong", "연산3동"), ("yeonsan-4-dong", "연산4동"), ("yeonsan-5-dong", "연산5동"), ("yeonsan-6-dong", "연산6동"), ("yeonsan-8-dong", "연산8동"), ("yeonsan-9-dong", "연산9동"),
    ]),
    "suyeong-gu": ("수영구", [
        ("namcheon-1-dong", "남천1동"), ("namcheon-2-dong", "남천2동"), ("suyeong-dong", "수영동"), ("mangmi-1-dong", "망미1동"), ("mangmi-2-dong", "망미2동"), ("gwangan-1-dong", "광안1동"), ("gwangan-2-dong", "광안2동"), ("gwangan-3-dong", "광안3동"), ("gwangan-4-dong", "광안4동"), ("millak-dong", "민락동"),
    ]),
    "sasang-gu": ("사상구", [
        ("samnak-dong", "삼락동"), ("mora-1-dong", "모라1동"), ("mora-3-dong", "모라3동"), ("deokpo-1-dong", "덕포1동"), ("deokpo-2-dong", "덕포2동"), ("gwaebeop-dong", "괘법동"), ("gamjeon-dong", "감전동"), ("jurye-1-dong", "주례1동"), ("jurye-2-dong", "주례2동"), ("jurye-3-dong", "주례3동"), ("hakjang-dong", "학장동"), ("eomgung-dong", "엄궁동"),
    ]),
    "gijang-gun": ("기장군", [
        ("gijang-eup", "기장읍"), ("jangan-eup", "장안읍"), ("jeonggwan-eup", "정관읍"), ("ilgwang-eup", "일광읍"), ("cheolma-myeon", "철마면"),
    ]),
}

GRADES = {
    "elementary": {
        "label": "초등", "eng": "ELEMENTARY", "years": "초1–초6",
        "tags": ["초등 수학수업", "초등 수학공부", "초등 기초수학"],
        "title_tail": "초등 수학수업·기초수학·수학공부",
        "summary": "{r} 초등 수학수업은 연산과 문장제 같은 기초수학을 탄탄히 다지고, 스스로 풀이를 설명하는 수학공부 습관을 만드는 데 집중합니다.",
        "points": [
            ("{r} 초등 수학수업", "교과서 개념을 그림과 생활 예시로 먼저 이해하고, 학생이 직접 말로 풀이를 설명하며 수업합니다."),
            ("초등 기초수학", "덧셈·뺄셈부터 곱셈·나눗셈, 분수와 소수까지 연산의 정확도와 속도를 함께 다집니다."),
            ("초등 수학공부 습관", "하루 분량의 과제와 오답 정리로 혼자서도 수학공부를 이어가는 습관을 만듭니다."),
            ("문장제·서술형", "긴 문제를 읽고 조건을 정리해 식으로 옮기는 과정을 단계별로 연습합니다."),
            ("중등 수학 준비", "초5·초6 학생은 분수·비율을 마무리하고 중1 수학으로 자연스럽게 이어지도록 준비합니다."),
            ("보호자 피드백", "수업 내용과 이해도, 다음 목표를 정기적으로 공유해 집에서도 도울 수 있게 합니다."),
        ],
        "years_detail": [
            ("초1·초2", "수 감각과 덧셈·뺄셈, 시계·길이 같은 생활 속 수학을 놀이처럼 익힙니다."),
            ("초3·초4", "곱셈·나눗셈과 분수의 기초, 도형 개념을 정확하게 다집니다."),
            ("초5·초6", "분수·소수 연산, 비와 비율을 마무리하고 중등 수학을 준비합니다."),
        ],
        "school_copy": "학교 교과서 진도와 단원평가 일정에 맞춰 개념과 연산을 함께 다집니다.",
        "faq": ("초등 수학과외는 언제 시작하는 게 좋나요?", "연산 실수가 잦거나 문장제를 어려워할 때, 또는 초5·초6에 중등 수학을 준비할 때 많이 시작합니다. 체험수업에서 현재 수준을 먼저 확인한 뒤 수업 방향을 안내합니다."),
    },
    "middle": {
        "label": "중등", "eng": "MIDDLE SCHOOL", "years": "중1–중3",
        "tags": ["중등 수학수업", "중등 수학공부", "중등 기초수학", "중등 수학내신"],
        "title_tail": "중등 수학내신·수학수업·기초수학",
        "summary": "{r} 중등 수학수업은 학교 진도에 맞춘 개념 정리와 학교별 수학내신 대비, 고등 수학으로 이어지는 기초수학 보완을 함께 진행합니다.",
        "points": [
            ("{r} 중등 수학수업", "학교 진도에 맞춰 개념 → 대표 유형 → 서술형 순서로 단계를 밟아 수업합니다."),
            ("중등 수학내신 대비", "학교 교과서와 부교재, 기출 경향을 확인해 중간·기말고사와 서술형 평가를 준비합니다."),
            ("중등 기초수학", "분수·비율처럼 초등 과정에서 생긴 빈틈과 방정식·함수의 기초를 다시 채웁니다."),
            ("중등 수학공부 방법", "개념 노트와 오답 원인 분류, 주간 점검으로 스스로 공부하는 방법을 익힙니다."),
            ("고등 수학 연결", "중3 과정은 고1 공통수학과 이어지는 단원을 중심으로 선행과 복습을 조절합니다."),
            ("보호자 피드백", "시험 결과와 단원별 이해도, 다음 목표를 정기적으로 공유합니다."),
        ],
        "years_detail": [
            ("중1", "소인수분해, 정수와 유리수, 일차방정식, 좌표평면과 그래프를 개념부터 정리합니다."),
            ("중2", "식의 계산, 연립방정식, 일차함수, 확률 등 내신 핵심 단원을 집중 대비합니다."),
            ("중3", "제곱근과 실수, 인수분해, 이차방정식·이차함수, 삼각비로 고등 수학을 준비합니다."),
        ],
        "school_copy": "학교별 교과서·부교재와 기출 경향을 확인해 중간·기말고사 수학내신을 대비합니다.",
        "faq": ("중등 수학내신은 어떻게 대비하나요?", "학교 교과서와 부교재, 기출 경향을 먼저 확인하고 시험 범위 단원을 개념 → 유형 → 서술형 순서로 반복합니다. 시험 직전에는 실전처럼 시간을 재고 풀어 보며 실수를 줄입니다."),
    },
    "high": {
        "label": "고등", "eng": "HIGH SCHOOL", "years": "고1–고3",
        "tags": ["고등 수학수업", "고등 수학공부", "고등 기초수학", "고등 수학내신", "고등 수능대비", "고등 수능수학"],
        "title_tail": "고등 수학내신·수능대비·수능수학",
        "summary": "{r} 고등 수학수업은 수학내신과 수능대비를 목표에 맞춰 병행합니다. 수능수학 기출 분석과 모의고사 오답 관리로 실전 점수를 끌어올립니다.",
        "points": [
            ("{r} 고등 수학수업", "고1 공통수학부터 고3 선택과목까지 학생의 학년과 목표 등급에 맞춰 수업을 설계합니다."),
            ("고등 수학내신", "학교별 기출과 부교재, 서술형 채점 기준을 분석해 중간·기말고사를 대비합니다."),
            ("수능대비 · 수능수학", "수능수학 기출 분석, 모의고사 오답 관리, 시간 배분 훈련으로 실전 점수를 올립니다."),
            ("고등 기초수학", "인수분해·함수처럼 중등 과정의 빈틈부터 다시 잡아 고등 개념이 쌓이도록 합니다."),
            ("고등 수학공부 전략", "내신 기간과 모의고사 일정에 맞춰 주간 학습량과 과목 비중을 조정합니다."),
            ("고난도 문항 훈련", "조건을 해석하고 발상을 이어가는 과정을 말로 설명하며 고난도 문제에 대비합니다."),
        ],
        "years_detail": [
            ("고1", "공통수학 개념과 첫 내신을 안정적으로 잡고, 중등 기초수학의 빈틈을 보완합니다."),
            ("고2", "선택과목 내신과 모의고사를 함께 대비하며 수능수학의 기본기를 만듭니다."),
            ("고3", "수능대비 기출 분석과 실전 모의고사, 수시 내신 마무리를 목표에 맞춰 진행합니다."),
        ],
        "school_copy": "학교별 기출과 부교재, 서술형 평가를 분석해 수학내신을 준비하고 수능대비를 병행합니다.",
        "faq": ("고등 수학내신과 수능대비를 함께 할 수 있나요?", "가능합니다. 학기 중에는 수학내신 비중을 높이고, 시험이 끝난 뒤와 방학에는 수능수학 기출과 모의고사 중심으로 비중을 조정합니다."),
    },
}

# 전국초중등학교위치표준데이터(2026-10-26)에서 추출한 운영 중인 부산 초·중·고
SCHOOLS = json.loads((ROOT / "data" / "schools-busan.json").read_text(encoding="utf-8"))
SCHOOL_SOURCE = "전국초중등학교위치표준데이터(2026-10-26 기준)"
SCHOOL_LEVELS = {"elementary": "초등학교", "middle": "중학교", "high": "고등학교"}
# 행정동 이름이 법정동과 다르게 묶인 곳
DONG_ALIASES = {"금사회동동": ["금사동", "회동동"], "청룡노포동": ["청룡동", "노포동"], "남항동": ["남항동", "대교동", "대평동"],
                "수민동": ["수안동", "낙민동"], "복산동": ["복천동", "칠산동"], "선두구동": ["선동", "두구동"],
                "가락동": ["죽림동", "식만동", "죽동동", "봉림동"], "가덕도동": ["성북동", "눌차동", "천성동", "대항동", "동선동"]}

DONG_INTROS = [
    "{d}에서 수학과외를 찾고 계신가요? 초등 기초수학부터 중등 수학내신, 고등 수능수학까지 학생의 현재 위치를 먼저 진단하고 1:1로 수업합니다.",
    "{g} {d} 학생의 학교 진도와 시험 일정에 맞춘 1:1 수학수업입니다. 개념을 외우기보다 이해하고, 스스로 풀어내는 수학공부 습관을 만듭니다.",
    "{d} 초등·중등·고등 학생을 위한 맞춤 수학과외입니다. 막힌 단원은 기초수학부터 다시 채우고, 내신과 수능대비는 목표 등급에 맞춰 설계합니다.",
    "같은 학년이라도 막히는 지점은 다릅니다. {d} 학생 한 명 한 명의 풀이 과정을 확인하고, 필요한 개념과 문제 유형을 골라 1:1 수학수업을 진행합니다.",
]


def jsonld(data):
    return '  <script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "</script>\n"


def breadcrumb_ld(crumbs):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": name, "item": SITE + path} for i, (name, path) in enumerate(crumbs)]}


def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


def common_faqs(r):
    return [
        (f"{r} 수학과외는 어떤 학년까지 가능한가요?", "초등 1학년부터 고등 3학년까지 가능합니다. 초등 기초수학, 중등 수학내신, 고등 수능대비·수능수학까지 학년과 목표에 맞춰 1:1로 수업합니다."),
        ("수업은 어디에서 진행되나요?", "학생의 지역과 일정에 따라 방문 수업 또는 온라인 수업으로 협의합니다. 상담 시 가장 편한 방식을 알려주세요."),
        ("체험수업은 어떻게 신청하나요?", f"{PHONE}로 전화 주시면 학년과 현재 고민을 듣고 체험수업 일정을 조율합니다. 체험수업에서 풀이 과정을 확인한 뒤 수업 방향을 안내합니다."),
    ]


def write_page(path, *, title, description, crumbs, category, eyebrow, h1, h1_em, hero_copy, hero_label, local_hero, sections, faqs, cta_region):
    url = SITE + path
    crumb_html = ' <span aria-hidden="true">›</span> '.join(
        f'<a href="{p}">{n}</a>' if i < len(crumbs) - 1 else f'<span aria-current="page">{n}</span>'
        for i, (n, p) in enumerate(crumbs))
    faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    section_html = "".join(f"    {s}\n" for s in sections if s)
    hero_class = "region-hero local-hero" if local_hero else "region-hero"
    html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{BRAND}">
  <meta property="og:locale" content="ko_KR">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{url}">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="stylesheet" href="/region.css">
{jsonld(breadcrumb_ld(crumbs))}{jsonld(faq_ld(faqs))}</head>
<body>
  <header class="region-header"><a class="brand" href="/"><span class="brand-mark" aria-hidden="true">想</span><span>{BRAND}</span></a><a class="category-link" href="{category[1]}">{category[0]}</a><a class="header-phone" href="{TEL}">전화 상담 {PHONE}</a></header>
  <nav class="breadcrumb" aria-label="현재 위치">{crumb_html}</nav>
  <main>
    <section class="{hero_class}" data-region="{hero_label}"><p class="eyebrow">{eyebrow}</p><h1>{h1}<br><em>{h1_em}</em></h1><p>{hero_copy}</p><div class="hero-actions"><a class="phone-button" href="{TEL}">체험수업 상담 {PHONE}</a><a class="sub-link" href="#guide">수업 안내 보기 ↓</a></div></section>
{section_html}    <section class="faq-block"><p class="section-label">FAQ</p><h2>{cta_region} 수학과외<br>자주 묻는 질문</h2><div class="faq-items">{faq_html}</div></section>
    <section class="region-cta"><h2>{cta_region} 수학과외 체험수업,<br>전화로 먼저 상담하세요.</h2><a class="phone-button" href="{TEL}">{PHONE}</a></section>
  </main>
  <footer class="region-footer"><span>{BRAND} · 초등·중등·고등 1:1 맞춤 수학 코칭</span><span>© 2026 Busan Math Tutoring.</span></footer><a class="floating-phone" href="{TEL}">체험수업 전화 상담 {PHONE}</a>
</body>
</html>
"""
    out = ROOT / path.strip("/") / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8", newline="\n")
    return path


def grade_cards(r, base, base_name, anchor_ids=False):
    cards = []
    for key, g in GRADES.items():
        tags = "".join(f"<li>{t}</li>" for t in g["tags"])
        id_attr = f' id="{key}"' if anchor_ids else ""
        cards.append(
            f'<article class="grade-card"{id_attr}><span class="grade-years">{g["years"]}</span><h3>{r} {g["label"]} 수학과외</h3>'
            f'<p>{g["summary"].format(r=r)}</p><ul class="tag-list">{tags}</ul>'
            f'<a class="more-link" href="{base}{key}/">{base_name} {g["label"]} 수학 자세히 보기 →</a></article>')
    return f'<div class="grade-grid">{"".join(cards)}</div>'


def process_section(r):
    return (f'<section class="region-content"><div class="intro"><div><p class="section-label">TRIAL LESSON</p><h2>{r} 체험수업에서<br>확인하는 세 가지</h2></div>'
            '<p class="intro-copy">현재 개념 이해도, 문제를 읽고 식을 세우는 과정, 오답을 다시 풀어내는 습관을 확인합니다. 학생에게 필요한 수업 방향과 학습 계획을 상담해 드립니다.</p></div>'
            '<div class="feature-grid"><article><span>01 / DIAGNOSIS</span><h3>현재 실력 진단</h3><p>개념 이해, 식 세우기, 풀이 습관을 함께 확인합니다.</p></article>'
            '<article><span>02 / LESSON</span><h3>1:1 체험수업</h3><p>직접 설명하고 질문하는 코칭 수업을 경험합니다.</p></article>'
            '<article><span>03 / ROADMAP</span><h3>맞춤 학습 설계</h3><p>학교 진도와 목표에 맞춰 보완할 단원과 수업 방향을 안내합니다.</p></article></div></section>')


def legal_dongs(dong):
    return DONG_ALIASES.get(dong, [dong, re.sub(r"\d+(?=동$)", "", dong)])


def school_section(r, schools, levels, title, copy):
    cols = []
    for key in levels:
        names = [s["name"] for s in schools[key]]
        if not names:
            continue
        items = "".join(f"<li>{n}</li>" for n in names)
        cols.append(f'<div class="school-col"><h3>{r} {SCHOOL_LEVELS[key]} <span>{len(names)}곳</span></h3><ul class="school-list">{items}</ul></div>')
    if not cols:
        return None
    return (f'<section class="school-section"><p class="section-label">SCHOOLS</p><h2>{title}</h2><p class="school-copy">{copy}</p>'
            f'<div class="school-grid">{"".join(cols)}</div><p class="school-source">학교 목록 출처: {SCHOOL_SOURCE}</p></section>')


def links_section(label, title, links, light=False):
    current = ' aria-current="page"'
    items = "".join(f'<a href="{href}"{current if cur else ""}>{text}</a>' for text, href, cur in links)
    cls = "area-section local-area-section" if light else "area-section"
    return f'<section class="{cls}"><p class="section-label">{label}</p><h2>{title}</h2><div class="area-list">{items}</div></section>'


def grade_page(region_full, r, base, key, child_links, child_title, crumbs, category, eng_region, schools=None):
    g = GRADES[key]
    path = f"{base}{key}/"
    points = "".join(f'<article><span>{i + 1:02d}</span><h3>{t.format(r=r)}</h3><p>{d}</p></article>' for i, (t, d) in enumerate(g["points"]))
    years = "".join(f'<div class="year-row"><h3>{r} {y} 수학과외</h3><p>{d}</p></div>' for y, d in g["years_detail"])
    others = [(f"{r} {GRADES[k]['label']} 수학과외", f"{base}{k}/", k == key) for k in GRADES]
    subjects = ", ".join(g["tags"][1:])
    sections = [
        f'<section id="guide" class="region-content"><div class="intro"><div><p class="section-label">{g["eng"]} MATH</p><h2>{r} {g["label"]} 수학,<br>어떻게 수업하나요?</h2></div>'
        f'<p class="intro-copy">{g["summary"].format(r=r)} 체험수업에서 풀이 과정을 확인하고 학생에게 맞는 학습 계획을 안내합니다.</p></div><div class="point-grid">{points}</div></section>',
        f'<section class="year-section"><p class="section-label">{g["years"]} BY GRADE</p><h2>{r} 학년별 {g["label"]} 수학과외</h2><div class="year-list">{years}</div></section>',
        links_section("OTHER GRADES", f"{r} 학년별 수학과외", others, light=True),
        links_section(f"{eng_region} AREAS", child_title, child_links),
    ]
    level = SCHOOL_LEVELS[key]
    names = [s["name"] for s in schools[key]] if schools else []
    school_desc = ""
    faqs = [g["faq"]] + common_faqs(r)[1:]
    if names:
        sections.insert(2, school_section(r, schools, [key], f"{r} {level} {g['label']} 수학과외",
                                          f"{r}에 있는 {level} {len(names)}곳 학생 모두 1:1 {g['label']} 수학과외를 받을 수 있습니다. {g['school_copy']}"))
        examples = "·".join(names[:2])
        school_desc = f" {examples} 등 {r} {level} 학생 맞춤."
        faqs.insert(1, (f"{examples} 학생도 수업할 수 있나요?",
                        f"네. {examples}를 포함해 {r} {level} {len(names)}곳 학생 모두 가능합니다. {g['school_copy']}"))
    return write_page(
        path,
        title=f"{region_full} {g['label']} 수학과외 | {g['title_tail']} 1:1",
        description=f"{region_full} {g['label']} 수학과외. {g['years']} 학생을 위한 1:1 {g['label']} 수학수업으로 {subjects}까지 학년별로 맞춤 지도합니다.{school_desc} 상담 {PHONE}.",
        crumbs=crumbs + [(f"{g['label']} 수학과외", path)], category=category,
        eyebrow=f"BUSAN {eng_region} · {g['eng']} MATH" if eng_region != "BUSAN" else f"BUSAN · {g['eng']} MATH",
        h1=region_full, h1_em=f"{g['label']} 수학과외",
        hero_copy=f"{g['years']} 학생의 학년과 목표에 맞춘 1:1 {g['label']} 수학수업. {subjects}까지 함께 준비합니다.",
        hero_label=g["label"], local_hero=len(region_full) > 6, sections=sections,
        faqs=faqs, cta_region=f"{r} {g['label']}")


def main():
    pages = []
    busan_crumbs = [("홈", "/"), ("부산", "/busan/")]

    # 부산 학년별 허브: /busan/elementary/ 등
    for key, g in GRADES.items():
        children = [(f"{name} {g['label']} 수학과외", f"/busan/{slug}/{key}/", False) for slug, (name, _) in DISTRICTS.items()]
        pages.append(grade_page("부산", "부산", "/busan/", key, children, f"부산 구·군별 {g['label']} 수학과외",
                                busan_crumbs, ("부산 지역 안내", "/busan/"), "BUSAN"))

    # 부산 지역 허브: /busan/
    matrix = "".join(
        f'<div class="matrix-row"><a class="matrix-head" href="/busan/{slug}/">{name} 수학과외</a>'
        + "".join(f'<a href="/busan/{slug}/{k}/">{name} {GRADES[k]["label"]}</a>' for k in GRADES) + "</div>"
        for slug, (name, _) in DISTRICTS.items())
    pages.append(write_page(
        "/busan/",
        title="부산 수학과외 지역별 안내 | 16개 구·군 초등·중등·고등 1:1 수학",
        description=f"부산 16개 구·군 수학과외 안내. 초등 기초수학, 중등 수학내신, 고등 수능대비·수능수학까지 지역별·학년별 1:1 수학수업을 확인하세요. 상담 {PHONE}.",
        crumbs=busan_crumbs, category=("지역별 페이지", "/busan/"),
        eyebrow="BUSAN · 16 LOCAL MATH COACHING GUIDES", h1="부산 지역별", h1_em="수학과외 안내",
        hero_copy="거주 지역과 학년을 선택해 초등·중등·고등 1:1 수학수업과 체험수업 상담 방법을 확인하세요.",
        hero_label="부산", local_hero=False,
        sections=[
            f'<section id="guide" class="grade-section"><p class="section-label">BY GRADE</p><h2>부산 학년별 수학과외</h2>{grade_cards("부산", "/busan/", "부산")}</section>',
            links_section("BUSAN 16 AREAS", "수업 지역을 선택하세요.", [(n, f"/busan/{s}/", False) for s, (n, _) in DISTRICTS.items()]),
            f'<section class="matrix-section"><p class="section-label">AREA × GRADE</p><h2>구·군별 학년 수학과외 바로가기</h2><div class="matrix">{matrix}</div></section>',
            process_section("부산"),
        ],
        faqs=common_faqs("부산"), cta_region="부산"))

    for slug, (gu, areas) in DISTRICTS.items():
        base = f"/busan/{slug}/"
        eng = slug.upper()
        gu_crumbs = busan_crumbs + [(gu, base)]

        # 구·군 학년별 페이지: /busan/haeundae-gu/high/ 등
        for key, g in GRADES.items():
            children = [(f"{name} {g['label']} 수학", f"{base}{aslug}/#{key}", False) for aslug, name in areas]
            pages.append(grade_page(f"부산 {gu}", gu, base, key, children, f"{gu} 동·읍·면별 {g['label']} 수학과외",
                                    gu_crumbs, (f"{gu} 지역 안내", base), eng, SCHOOLS[slug]))

        # 구·군 메인
        names = "·".join(n for _, n in areas[:4])
        pages.append(write_page(
            base,
            title=f"부산 {gu} 수학과외 | 초등·중등·고등 1:1 수학수업·내신·수능대비",
            description=f"부산 {gu} 수학과외 안내. {names} 등 {gu} 초등 기초수학, 중등 수학내신, 고등 수능대비·수능수학까지 1:1 맞춤 수학수업. 체험수업 상담 {PHONE}.",
            crumbs=gu_crumbs, category=("부산 지역 안내", "/busan/"),
            eyebrow=f"BUSAN {eng} · 1:1 MATH COACHING", h1=f"부산 {gu}", h1_em="수학과외 안내",
            hero_copy=f"{gu} 초·중·고 학생의 개념 이해도와 풀이 습관을 진단하고, 학교 진도와 목표에 맞는 1:1 수학수업을 설계합니다.",
            hero_label=gu, local_hero=False,
            sections=[
                f'<section id="guide" class="grade-section"><p class="section-label">{eng} BY GRADE</p><h2>{gu} 학년별 수학과외</h2>{grade_cards(gu, base, gu)}</section>',
                school_section(gu, SCHOOLS[slug], SCHOOL_LEVELS, f"{gu} 초·중·고등학교 수학과외",
                               f"{gu}에 있는 " + ", ".join(f"{SCHOOL_LEVELS[k]} {len(SCHOOLS[slug][k])}곳" for k in SCHOOL_LEVELS)
                               + " 학생 모두 1:1 수학과외를 받을 수 있습니다. 다니는 학교의 교과서와 부교재, 시험 범위에 맞춰 수업합니다."),
                links_section(f"{gu} LOCAL AREAS", f"{gu} 동·읍·면별 수학과외", [(n, f"{base}{s}/", False) for s, n in areas], light=True),
                process_section(gu),
                links_section("BUSAN AREA", "부산 다른 지역 수학과외", [(n, f"/busan/{s}/", s == slug) for s, (n, _) in DISTRICTS.items()]),
            ],
            faqs=common_faqs(gu), cta_region=gu))

        # 동·읍·면 페이지
        for i, (aslug, dong) in enumerate(areas):
            path = f"{base}{aslug}/"
            intro = DONG_INTROS[sum(map(ord, aslug)) % len(DONG_INTROS)].format(d=dong, g=gu)
            near = list(dict.fromkeys(areas[(i + k) % len(areas)][1] for k in (-1, 1, 2) if areas[(i + k) % len(areas)][0] != aslug))
            near_txt = f" {dong} 외에도 {'·'.join(near)} 등 {gu} 인근 학생도 상담할 수 있습니다." if near else ""
            siblings = [(f"{gu} 전체", base, False)] + [(n, f"{base}{s}/", s == aslug) for s, n in areas]
            legal = list(dict.fromkeys(legal_dongs(dong)))
            nearby = {k: [s for s in SCHOOLS[slug][k] if s["dong"] in legal] for k in SCHOOL_LEVELS}
            near_schools = school_section(dong, nearby, SCHOOL_LEVELS, f"{dong} 인근 학교 수학과외",
                                          f"{'·'.join(legal)}에 있는 학교입니다. 이 학교 학생은 물론 {gu} 다른 학교 학생도 학교 진도와 시험 범위에 맞춰 1:1로 수업합니다.")
            pages.append(write_page(
                path,
                title=f"부산 {gu} {dong} 수학과외 | 초등·중등·고등 1:1 수학수업",
                description=f"부산 {gu} {dong} 수학과외. 초등 기초수학·수학공부, 중등 수학내신, 고등 수능대비·수능수학까지 학년별 1:1 수학수업. 체험수업 상담 {PHONE}.",
                crumbs=gu_crumbs + [(dong, path)], category=(f"{gu} 지역 안내", base),
                eyebrow=f"BUSAN {aslug.upper()} · 1:1 MATH COACHING", h1=f"부산 {gu} {dong}", h1_em="수학과외 안내",
                hero_copy=f"{dong} 초·중·고 학생의 개념 이해도와 풀이 습관을 진단하고, 목표에 맞는 1:1 수학수업을 설계합니다.",
                hero_label=dong, local_hero=True,
                sections=[
                    f'<section class="region-content"><div class="intro"><div><p class="section-label">{dong} MATH COACHING</p><h2>{dong} 학생에게 맞춘<br>1:1 수학수업</h2></div><p class="intro-copy">{intro}{near_txt}</p></div></section>',
                    f'<section id="guide" class="grade-section"><p class="section-label">BY GRADE</p><h2>{dong} 학년별 수학과외</h2>{grade_cards(dong, base, gu, anchor_ids=True)}</section>',
                    near_schools,
                    process_section(dong),
                    links_section(f"{gu} LOCAL AREAS", f"{gu} 지역별 수학과외", siblings),
                ],
                faqs=common_faqs(dong), cta_region=dong))

    def priority(p):
        return "0.9" if p == "/busan/" else "0.8" if p.count("/") == 3 else "0.7"

    entries = [f"  <url><loc>{SITE}/</loc><lastmod>{LASTMOD}</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>"]
    entries += [f"  <url><loc>{SITE}{p}</loc><lastmod>{LASTMOD}</lastmod><changefreq>weekly</changefreq><priority>{priority(p)}</priority></url>"
                for p in sorted(pages, key=lambda p: (p.count("/"), p))]
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(entries) + "\n</urlset>\n",
        encoding="utf-8", newline="\n")
    print(f"Generated {len(pages)} pages.")


if __name__ == "__main__":
    main()
