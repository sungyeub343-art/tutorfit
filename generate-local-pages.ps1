$ErrorActionPreference = "Stop"

$districts = [ordered]@{
  "jung-gu" = @{ Name = "중구"; Areas = [ordered]@{
    "jungang-dong"="중앙동"; "donggwang-dong"="동광동"; "daecheong-dong"="대청동"; "bosu-dong"="보수동"; "bupyeong-dong"="부평동"; "gwangbok-dong"="광복동"; "nampo-dong"="남포동"; "yeongju-1-dong"="영주1동"; "yeongju-2-dong"="영주2동"
  }}
  "seo-gu" = @{ Name = "서구"; Areas = [ordered]@{
    "dongdaesin-1-dong"="동대신1동"; "dongdaesin-2-dong"="동대신2동"; "dongdaesin-3-dong"="동대신3동"; "seodaesin-1-dong"="서대신1동"; "seodaesin-3-dong"="서대신3동"; "seodaesin-4-dong"="서대신4동"; "bumin-dong"="부민동"; "ami-dong"="아미동"; "chojang-dong"="초장동"; "chungmu-dong"="충무동"; "nambumin-1-dong"="남부민1동"; "nambumin-2-dong"="남부민2동"; "amnam-dong"="암남동"
  }}
  "dong-gu" = @{ Name = "동구"; Areas = [ordered]@{
    "choryang-1-dong"="초량1동"; "choryang-2-dong"="초량2동"; "choryang-3-dong"="초량3동"; "choryang-6-dong"="초량6동"; "sujeong-1-dong"="수정1동"; "sujeong-2-dong"="수정2동"; "sujeong-4-dong"="수정4동"; "sujeong-5-dong"="수정5동"; "jwacheon-dong"="좌천동"; "beomil-1-dong"="범일1동"; "beomil-2-dong"="범일2동"; "beomil-5-dong"="범일5동"
  }}
  "yeongdo-gu" = @{ Name = "영도구"; Areas = [ordered]@{
    "namhang-dong"="남항동"; "yeongseon-1-dong"="영선1동"; "yeongseon-2-dong"="영선2동"; "sinseon-dong"="신선동"; "bongnae-1-dong"="봉래1동"; "bongnae-2-dong"="봉래2동"; "cheonghak-1-dong"="청학1동"; "cheonghak-2-dong"="청학2동"; "dongsam-1-dong"="동삼1동"; "dongsam-2-dong"="동삼2동"; "dongsam-3-dong"="동삼3동"
  }}
  "busanjin-gu" = @{ Name = "부산진구"; Areas = [ordered]@{
    "bujeon-1-dong"="부전1동"; "bujeon-2-dong"="부전2동"; "yeonji-dong"="연지동"; "choeup-dong"="초읍동"; "yangjeong-1-dong"="양정1동"; "yangjeong-2-dong"="양정2동"; "jeonpo-1-dong"="전포1동"; "jeonpo-2-dong"="전포2동"; "buam-1-dong"="부암1동"; "buam-3-dong"="부암3동"; "danggam-1-dong"="당감1동"; "danggam-2-dong"="당감2동"; "danggam-4-dong"="당감4동"; "gaya-1-dong"="가야1동"; "gaya-2-dong"="가야2동"; "gaegeum-1-dong"="개금1동"; "gaegeum-2-dong"="개금2동"; "gaegeum-3-dong"="개금3동"; "beomcheon-1-dong"="범천1동"; "beomcheon-2-dong"="범천2동"
  }}
  "dongnae-gu" = @{ Name = "동래구"; Areas = [ordered]@{
    "sumin-dong"="수민동"; "boksan-dong"="복산동"; "myeongnyun-dong"="명륜동"; "oncheon-1-dong"="온천1동"; "oncheon-2-dong"="온천2동"; "oncheon-3-dong"="온천3동"; "sajik-1-dong"="사직1동"; "sajik-2-dong"="사직2동"; "sajik-3-dong"="사직3동"; "anrak-1-dong"="안락1동"; "anrak-2-dong"="안락2동"; "myeongjang-1-dong"="명장1동"; "myeongjang-2-dong"="명장2동"
  }}
  "nam-gu" = @{ Name = "남구"; Areas = [ordered]@{
    "daeyeon-1-dong"="대연1동"; "daeyeon-3-dong"="대연3동"; "daeyeon-4-dong"="대연4동"; "daeyeon-5-dong"="대연5동"; "daeyeon-6-dong"="대연6동"; "yongho-1-dong"="용호1동"; "yongho-2-dong"="용호2동"; "yongho-3-dong"="용호3동"; "yongho-4-dong"="용호4동"; "yongdang-dong"="용당동"; "gamman-1-dong"="감만1동"; "gamman-2-dong"="감만2동"; "uam-dong"="우암동"; "munhyeon-1-dong"="문현1동"; "munhyeon-2-dong"="문현2동"; "munhyeon-3-dong"="문현3동"; "munhyeon-4-dong"="문현4동"
  }}
  "buk-gu" = @{ Name = "북구"; Areas = [ordered]@{
    "gupo-1-dong"="구포1동"; "gupo-2-dong"="구포2동"; "gupo-3-dong"="구포3동"; "geumgok-dong"="금곡동"; "hwamyeong-1-dong"="화명1동"; "hwamyeong-2-dong"="화명2동"; "hwamyeong-3-dong"="화명3동"; "deokcheon-1-dong"="덕천1동"; "deokcheon-2-dong"="덕천2동"; "deokcheon-3-dong"="덕천3동"; "mandeok-1-dong"="만덕1동"; "mandeok-2-dong"="만덕2동"; "mandeok-3-dong"="만덕3동"
  }}
  "haeundae-gu" = @{ Name = "해운대구"; Areas = [ordered]@{
    "u-1-dong"="우1동"; "u-2-dong"="우2동"; "u-3-dong"="우3동"; "jung-1-dong"="중1동"; "jung-2-dong"="중2동"; "jwa-1-dong"="좌1동"; "jwa-2-dong"="좌2동"; "jwa-3-dong"="좌3동"; "jwa-4-dong"="좌4동"; "songjeong-dong"="송정동"; "bansong-1-dong"="반송1동"; "bansong-2-dong"="반송2동"; "banyeo-1-dong"="반여1동"; "banyeo-2-dong"="반여2동"; "banyeo-3-dong"="반여3동"; "banyeo-4-dong"="반여4동"; "jaesong-1-dong"="재송1동"; "jaesong-2-dong"="재송2동"
  }}
  "saha-gu" = @{ Name = "사하구"; Areas = [ordered]@{
    "goejeong-1-dong"="괴정1동"; "goejeong-2-dong"="괴정2동"; "goejeong-3-dong"="괴정3동"; "goejeong-4-dong"="괴정4동"; "dangni-dong"="당리동"; "hadan-1-dong"="하단1동"; "hadan-2-dong"="하단2동"; "sinpyeong-1-dong"="신평1동"; "sinpyeong-2-dong"="신평2동"; "jangnim-1-dong"="장림1동"; "jangnim-2-dong"="장림2동"; "dadae-1-dong"="다대1동"; "dadae-2-dong"="다대2동"; "gupyeong-dong"="구평동"; "gamcheon-1-dong"="감천1동"; "gamcheon-2-dong"="감천2동"
  }}
  "geumjeong-gu" = @{ Name = "금정구"; Areas = [ordered]@{
    "seo-1-dong"="서1동"; "seo-2-dong"="서2동"; "seo-3-dong"="서3동"; "geumsa-hoedong-dong"="금사회동동"; "bugok-1-dong"="부곡1동"; "bugok-2-dong"="부곡2동"; "bugok-3-dong"="부곡3동"; "bugok-4-dong"="부곡4동"; "jangjeon-1-dong"="장전1동"; "jangjeon-2-dong"="장전2동"; "seondugu-dong"="선두구동"; "cheongnyong-nopo-dong"="청룡노포동"; "namsan-dong"="남산동"; "guseo-1-dong"="구서1동"; "guseo-2-dong"="구서2동"; "geumseong-dong"="금성동"
  }}
  "gangseo-gu" = @{ Name = "강서구"; Areas = [ordered]@{
    "daejeo-1-dong"="대저1동"; "daejeo-2-dong"="대저2동"; "gangdong-dong"="강동동"; "myeongji-1-dong"="명지1동"; "myeongji-2-dong"="명지2동"; "garak-dong"="가락동"; "noksan-dong"="녹산동"; "gadeokdo-dong"="가덕도동"; "sinho-dong"="신호동"
  }}
  "yeonje-gu" = @{ Name = "연제구"; Areas = [ordered]@{
    "geoje-1-dong"="거제1동"; "geoje-2-dong"="거제2동"; "geoje-3-dong"="거제3동"; "geoje-4-dong"="거제4동"; "yeonsan-1-dong"="연산1동"; "yeonsan-2-dong"="연산2동"; "yeonsan-3-dong"="연산3동"; "yeonsan-4-dong"="연산4동"; "yeonsan-5-dong"="연산5동"; "yeonsan-6-dong"="연산6동"; "yeonsan-8-dong"="연산8동"; "yeonsan-9-dong"="연산9동"
  }}
  "suyeong-gu" = @{ Name = "수영구"; Areas = [ordered]@{
    "namcheon-1-dong"="남천1동"; "namcheon-2-dong"="남천2동"; "suyeong-dong"="수영동"; "mangmi-1-dong"="망미1동"; "mangmi-2-dong"="망미2동"; "gwangan-1-dong"="광안1동"; "gwangan-2-dong"="광안2동"; "gwangan-3-dong"="광안3동"; "gwangan-4-dong"="광안4동"; "millak-dong"="민락동"
  }}
  "sasang-gu" = @{ Name = "사상구"; Areas = [ordered]@{
    "samnak-dong"="삼락동"; "mora-1-dong"="모라1동"; "mora-3-dong"="모라3동"; "deokpo-1-dong"="덕포1동"; "deokpo-2-dong"="덕포2동"; "gwaebeop-dong"="괘법동"; "gamjeon-dong"="감전동"; "jurye-1-dong"="주례1동"; "jurye-2-dong"="주례2동"; "jurye-3-dong"="주례3동"; "hakjang-dong"="학장동"; "eomgung-dong"="엄궁동"
  }}
  "gijang-gun" = @{ Name = "기장군"; Areas = [ordered]@{
    "gijang-eup"="기장읍"; "jangan-eup"="장안읍"; "jeonggwan-eup"="정관읍"; "ilgwang-eup"="일광읍"; "cheolma-myeon"="철마면"
  }}
}

$root = if ($PSScriptRoot) { $PSScriptRoot } else { (Get-Location).Path }
$utf8 = New-Object System.Text.UTF8Encoding($false)
$sitemapEntries = New-Object System.Collections.Generic.List[string]
$generatedCount = 0

foreach ($districtSlug in $districts.Keys) {
  $district = $districts[$districtSlug]
  $districtName = $district.Name
  $areaLinks = ($district.Areas.GetEnumerator() | ForEach-Object { '<a href="{0}/">{1}</a>' -f $_.Key, $_.Value }) -join ""
  $districtPath = Join-Path $root "busan\$districtSlug\index.html"
  $districtHtml = [System.IO.File]::ReadAllText($districtPath)
  $districtHtml = [regex]::Replace($districtHtml, '(?s)\s*<section class="area-section local-area-section".*?</section>', '')
  $localSection = "`r`n    <section class=`"area-section local-area-section`"><p class=`"section-label`">$districtName LOCAL AREAS</p><h2>$districtName 동·읍·면 수학과외 안내</h2><div class=`"area-list`">$areaLinks</div></section>"
  $districtHtml = [regex]::Replace($districtHtml, '\s*<section class="region-cta">', "$localSection`r`n    <section class=`"region-cta`">")
  [System.IO.File]::WriteAllText($districtPath, $districtHtml, $utf8)

  foreach ($areaSlug in $district.Areas.Keys) {
    $areaName = $district.Areas[$areaSlug]
    $areaPath = Join-Path $root "busan\$districtSlug\$areaSlug"
    [System.IO.Directory]::CreateDirectory($areaPath) | Out-Null
    $siblingLinks = ($district.Areas.GetEnumerator() | ForEach-Object {
      $current = if ($_.Key -eq $areaSlug) { ' aria-current="page"' } else { '' }
      '<a href="../{0}/"{1}>{2}</a>' -f $_.Key, $current, $_.Value
    }) -join ""
    $canonical = "https://tutorfit.kr/busan/$districtSlug/$areaSlug/"
    $html = @"
<!doctype html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="부산 $districtName $areaName 초·중·고 학생을 위한 1:1 수학과외 체험수업 안내입니다.">
  <title>부산 $districtName $areaName 수학과외 체험수업 안내 | 부산 수학과외</title>
  <link rel="canonical" href="$canonical">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="../../../region.css">
</head>
<body>
  <header class="region-header"><a class="brand" href="/"><span class="brand-mark" aria-hidden="true">想</span><span>부산 수학과외</span></a><a class="category-link" href="/busan/$districtSlug/">$districtName 지역 안내</a><a class="header-phone" href="tel:01029283614">전화 상담 010-2928-3614</a></header>
  <main>
    <section class="region-hero local-hero" data-region="$areaName"><p class="eyebrow">BUSAN $($areaSlug.ToUpper()) · 1:1 MATH COACHING</p><h1>부산 $districtName $areaName<br><em>수학과외 체험수업 안내</em></h1><p>$areaName 초·중·고 학생의 현재 개념 이해도와 문제 해결 습관을 확인하고, 목표에 맞는 1:1 수업 방향을 함께 설계합니다.</p><div class="hero-actions"><a class="phone-button" href="tel:01029283614">체험수업 상담 010-2928-3614</a><a class="sub-link" href="#guide">수업 안내 보기 ↓</a></div></section>
    <section id="guide" class="region-content"><div class="intro"><div><p class="section-label">$areaName MATH COACHING</p><h2>$areaName 학생에게 맞춘<br>수학의 시작</h2></div><p class="intro-copy">초등 개념 형성부터 중등 내신, 고등 수학까지 학생별 진도와 취약점을 기준으로 수업합니다. 체험수업에서 풀이 과정을 살펴보고 $areaName 학생에게 필요한 학습 방향을 안내합니다.</p></div><div class="feature-grid"><article><span>01 / DIAGNOSIS</span><h3>현재 실력 진단</h3><p>개념 이해, 식 세우기, 풀이 습관을 함께 확인합니다.</p></article><article><span>02 / LESSON</span><h3>1:1 체험수업</h3><p>직접 설명하고 질문하는 코칭 수업을 경험합니다.</p></article><article><span>03 / ROADMAP</span><h3>맞춤 학습 설계</h3><p>학교 진도와 목표에 맞춰 보완할 단원과 수업 방향을 안내합니다.</p></article></div></section>
    <section class="area-section"><p class="section-label">$districtName LOCAL AREAS</p><h2>$districtName 지역별 수학과외 안내</h2><div class="area-list"><a href="../">$districtName 전체 안내</a>$siblingLinks</div></section>
    <section class="region-cta"><h2>$areaName 수학과외 체험수업,<br>전화로 먼저 상담하세요.</h2><a class="phone-button" href="tel:01029283614">010-2928-3614</a></section>
  </main>
  <footer class="region-footer"><span>부산 수학과외 · 1:1 맞춤 수학 코칭</span><span>© 2026 Busan Math Tutoring.</span></footer><a class="floating-phone" href="tel:01029283614">체험수업 전화 상담 010-2928-3614</a>
</body>
</html>
"@
    [System.IO.File]::WriteAllText((Join-Path $areaPath "index.html"), $html, $utf8)
    $sitemapEntries.Add("  <url><loc>$canonical</loc><lastmod>2026-09-28</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>")
    $generatedCount++
  }
}

$sitemapPath = Join-Path $root "sitemap.xml"
$sitemap = [System.IO.File]::ReadAllText($sitemapPath)
$sitemap = [regex]::Replace($sitemap, '(?s)\s*<!-- LOCAL_PAGES_START -->.*?<!-- LOCAL_PAGES_END -->', '')
$localSitemap = "`r`n  <!-- LOCAL_PAGES_START -->`r`n$($sitemapEntries -join "`r`n")`r`n  <!-- LOCAL_PAGES_END -->`r`n"
$sitemap = $sitemap.Replace('</urlset>', "$localSitemap</urlset>")
[System.IO.File]::WriteAllText($sitemapPath, $sitemap, $utf8)

Write-Output "Generated $generatedCount local pages."