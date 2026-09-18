<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0383.txt",
      "sha256": "f9e69192a9914b1975fadec7a7462e85e486b529cd60379e7fccf6baad16a594",
      "bytes": 15379
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "39c8213a294f988814a8e4a8e88bfd934b2108cb128356598956975758a71c5c",
      "bytes": 2221
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "200edd2279a24223fd79e93690e5c264b80b140ef9f855321330d3e948aec276",
      "bytes": 133089
    },
    {
      "path": "characters/Pill Physician.md",
      "sha256": "d66e5e77b1e5a18e59a85e7ec18ca850ea325a2ad74d5ee962acd1e06a144cd3",
      "bytes": 554
    },
    {
      "path": "characters/Wei Fenghu.md",
      "sha256": "123aacc02172fdc3c48cab016a2e603a0c3cd7db7857f77de722508aaea1c2b2",
      "bytes": 538
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c87ecc767c64345f1ef7963a5df13917b05754841b433c7b2a023ac2b15f1c63",
      "bytes": 103078
    }
  ],
  "estimated_tokens": 10020
}
-->

# Durable State Update — Chapter 383

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 383. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 383. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 383,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 383,
    "continuity_sources": [383],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.

## Prior durable context

```json
{
  "active_continuity": [
    "Jin Taekyung destroyed the three incomplete Liches serving the Arch Lich, collapsing the undead monster army at Chengdu International Airport.",
    "The incomplete Liches swore on the River of Death that their account of the Arch Lich's actions was truthful.",
    "The Skeleton Warlord absorbed a massive amount of death energy, grew much stronger, and is kept in Jin Taekyung's Inventory; Jin calls it Bones as a mocking pet name.",
    "Jin Taekyung is Level 121 and has acquired the Undead Hunter Title after completing the Unexpected Attack Quest.",
    "Team Leader Choi and Shao Shen survived the airport battle and met Jin after the fighting ended.",
    "Wei Fenghu is China's Minister of National Defense under the Central Military Commission and a four-star general.",
    "Wei Fenghu is taking Jin Taekyung to an operations headquarters where a jet and unidentified waiting people are present."
  ],
  "continuity_sources": [
    382,
    381
  ],
  "open_questions": [
    "Who is the Arch Lich, and what will happen after Jin Taekyung destroys its three servants?",
    "Who is everyone waiting for Jin Taekyung at the operations headquarters?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Who is the unidentified person directing Aehyang, and what are they planning?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?"
  ],
  "safe_through": 382,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon.",
    "Use Mimi for 미미 and Mimi-chan for 미미쨩; render 삼괴 as Third Fiend in singular references and Three Fiends in collective references.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, 신니 as Venerable Nun, 환영진 as illusion formation, and 이동진 as Moving Formation.",
    "Render 독룡각 as Poison Dragon Pavilion, 가주 대행 as Acting Family Head, 화룡갑 as Fire Dragon Armor, and 아크 리치 as Arch Lich.",
    "Render 사기 as death energy, 의념 as conveyed thoughts, 데스나이트 as Death Knight, and 골골 as Bones."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 환의 | **Pill Physician** | Title of the current Family Head of the Seongsu Jang Family. |
| 웨이펑후 | **Wei Fenghu** | Minister of National Defense under China's Central Military Commission. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 국밥 | **gukbap** | Korean dish of rice served in hot soup; footnoted in the reading copy. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 와이번 | **Wyvern** | High-tier dragonkin monster. |
| 수령님 | **Supreme Leader** | Title used in Taekyung's North Korean TV comparison. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 난충시 | **Nanchong City** | City near the disaster site shown in the reconnaissance footage. |
| 중화인민공화국 | **People's Republic of China** | Formal country name shouted by the Chinese Hunters. |
| 주석 | **Chairman** | Political title used for Xiao Yang. |
| 청두 | **Chengdu** | Administrative capital of Sichuan Province and destination airport city. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 청성산 | **Mount Qingcheng** | Mountain containing the Qingcheng Sect. |
| 국방부 | **Ministry of National Defense** | Government ministry referenced in Taekyung's comparison about the steady passage of time. |
| 중화 | **Zhonghua** | Patriotic term used in Shao Shen’s rallying speech. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Pill Physician.md

# Pill Physician (환의)

- **Safe through:** Chapter 375
- **Aliases:** None
- **Role:** Current Family Head of the Seongsu Jang Family in Shandong, who personally placed and signed the Thousand-Year Snow Ginseng in the casket entrusted to the Yongbong Escort Bureau.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** The Pill Physician heads the Seongsu Jang Family, a prestigious medical family in Shandong.

### Wei Fenghu.md

# Wei Fenghu (웨이펑후)

- **Safe through:** Chapter 382
- **Aliases:** None
- **Role:** Wei Fenghu is the Minister of National Defense under China's Central Military Commission and a four-star general.
- **Personality:** Courteous, reserved, and authoritative.
- **Voice:** Formal and measured, addressing Jin as Mr. Jin.
- **Relationships:** He has no established personal relationship with Jin Taekyung beyond their first meeting after the Chengdu airport battle.

## Korean source

```text
＃383화



웨이펑후가 준비해 두었다는 제트기는 생각했던 모습과는 상당한 차이가 있었다.

‘넓네. 화려하고.’

살짝 열린 출입문 너머로 고급스러운 테이블과 소위 말하는 회장님 의자가 보였다.

곁에 있던 최 팀장이 우리가 보고 있는 이게 한 대당 천억에 육박하는 비즈니스 제트기라는 걸 알려 주며 덧붙였다.

「국빈용으로나 쓰이는 기체를 여기서 볼 줄은 몰랐군요.」

웨이펑후가 담담하게 대꾸했다.

「당연한 일이오. 두 선생께서는 본국의 국빈이시니.」

“아.”

「덕분에 수많은 병사와 헌터들을 살릴 수 있었소. 나를 포함한 모두는 오늘의 도움을 절대 잊지 않을 거요.」

“……아, 예.”

그 전에 미세먼지와 역사 왜곡부터 좀 처리해 줬으면 좋겠는데.

내심 중국이 내가 알고 있는 것보다 더 양심적인 국가이길 바라며 기체에 몸을 실었다.

대기하던 조종사가 우리를 향해, 정확히는 웨이펑후를 향해 절도있는 동작으로 경례를 올렸다.

「오셨습니까, 국방부장 동지.」

「준비는?」

「본 기체를 포함한 호위기 모두 준비를 끝마쳤습니다. 명령만 내려 주시면 됩니다.」

호위라기에 뭔 소린가 했더니, 창밖 활주로에 날렵한 곡선을 자랑하는 전투기 다섯 대가 신호를 보내듯 불을 깜빡이는 것이 보였다.

‘뭐여, 저게.’

전쟁 영화에서나 보던 걸 여기서 보네. 당장 한판 뜨러 가기라도 하는 건가?

눈을 동그랗게 뜬 내 모습에 웨이펑후가 입을 열었다.

「아직 외부에는 정확히 알려지지 않았지만…… 알다시피 현재 쓰촨성은 전시 상황이오. 마법으로 인한 통신 방해와 비행 몬스터들의 습격까지 빈번하게 이루어지는 실정이니, 안전을 위해 호위는 필수지.」

“정말입니까?”

생각했던 것보다 상황이 심각하다.

우리야 청두 국제공항을 습격하러 온 와이번에게 겸사겸사 느낌으로 습격을 당한 거지만, 이게 쓰촨성 전역에서 벌어지는 일이라면 이야기가 달라진다.

「차라리 내가 거짓말을 하는 거라면 얼마나 좋겠소.」

현재 상황을 떠올리는 것만으로 지치는지, 부쩍 늙어 버린 웨이펑후가 푹신한 좌석 시트에 몸을 기댔다.

「자네와는 여기에서 작별해야 할 듯싶군. 조만간 다시 만나세. 샤오 쉔 대교(大校).」

우리와 달리 기체에 오르지 않은 한 사람, 샤오 쉔이 부동자세로 경례를 취했다.

「예. 조속히 임무를 마친 후 합류하겠습니다, 국방부장 동지. 그리고 두 선생님.」

「그래, 기대가 크네.」

상당한 전공을 세웠기 때문인지 전도유망한 젊은 헌터를 바라보는 웨이펑후의 입가에 흐뭇한 미소가 스쳤다.

최 팀장은 정중한 묵례로 인사를 대신했고, 나는 손을 흔들어 주었다.

“다음에 또 봐요. 오늘 아주 잘 싸웠어.”

단지 한 마디였을 뿐이었다.

하지만 내 말을 들은 샤오 쉔의 눈동자가 쟁반만큼 커졌다. 전기에 감전된 것처럼 몸을 부르르 떨던 그가 쩌렁쩌렁하게 외쳤다.

「가, 감사합니다! 진 선생님께서 실망하시는 일 없도록 모든 일에 견마지로(犬馬之勞)를 다하겠습니다!」

“……아니, 뭘 견마지로씩이나.”

「옥체 무사하시길 기원하겠습니다! 추웅! 성!」

“옥체라니. 그게 무슨…….”

빡!

「흡!」

“…….”

저건 잘못된 판단의 표본 같은데.

경례를 얼마나 세게 했는지 손날로 본인의 눈썹 부분을 때린 수준이다.

이를 악물고 아픔을 참는 샤오 쉔의 모습을 황당하게 바라보던 그때, 입구가 닫히고 우리가 탄 비즈니스 제트기가 천천히 이륙을 시작했다.

“저 친구도 뭐랄까, 그……. 캐릭터가 독특하네요.”

내 떨떠름한 말에 웨이펑후가 피식 웃었다.

「우상에게 칭찬을 들었으니 그럴 만도 하지 않겠소?」

“예?”

「본국에는 진 선생을 동경하는 젊은 헌터들이 많소. 저 친구도 예외는 아니지.」

뭐야, 나 한류 스타였어?

그나저나 이 양반, 나는 새도 떨어트린다는 포 스타치고 아랫사람에게 관심이 많은 것 같다.

아니면 샤오 쉔이 그만큼 기대받는 청년이거나.

아, 그런데…….

- 팀장님. 중앙군사위원회 국방부장이면 정확히 어느 정도예요? 제가 이쪽 편제를 잘 몰라서.

내 전음에 움찔한 최 팀장이 메시지 마법으로 대답했다.

- 우리나라로 치자면 국방부 장관입니다. 물론 이곳은 중국이고, 웨이펑후는 현 주석의 오른팔이니 그 권력이 훨씬 막대하죠.

- 아.

나랑 비슷하네. 난 국밥부 장관인데.

순대국 특 하나면 공깃밥 세 그릇 정도는 거뜬하다.

물론 웨이펑후는 손가락질 하나로 도시 세 개를 지워 버릴 수도 있겠지만.

그리고 지금, 막대한 권한을 지닌 중화인민공화국의 권력자가 우리를 향해 상반신을 기울이며 묻고 있다.

「가는 동안 나눠야 할 대화가 많은 것 같소만. 안 그렇소?」

최 팀장과 내가 진지하게 고개를 끄덕이며 입을 열었다.

「물론입니다. 우선 현재 쓰촨성의 상황이 정확히 어찌 돌아가는지부터 여쭤…….」

“그런데 혹시 삶은 달걀이랑 사이다 없나요. 열심히 싸웠더니 허기가 져서.”

“…….”

“…….”

없는 모양이다.

「있소.」

“……?”

“……?”

이게 있네.



* * *



중화인민공화국.

중국의 정식 명칭에서 알 수 있듯이 이 위엄 넘치는 대륙인들은 아직도 사회주의를 국가 이념으로 삼고 있었다.

지금으로부터 약 이십여 년 전, 종신 집권으로 독재의 기틀을 공고히 다졌던 당시 주석이 대격변 도중 사망하면서 훨씬 온건한 정권으로 권력이 이양되기는 했지만, 아직도 알맹이는 여전하다.

- 죽은 주석 이름이 뭐였죠? 핑핑이? 팽팽이?

웨이펑후의 말에 맞장구치던 최 팀장이 입술을 달싹였다. 경이로울 정도의 포커페이스다.

- ……혹시나 해서 드리는 말씀인데, 이곳에서 그런 말 꺼냈다가는 정말 큰일 납니다.

- 그래서 전음, 아니 메시지 마법으로 하잖아요.

- 주의하라는 말입니다. A급 이상의 뛰어난 마법사 중에는 메시지 마법을 도청할 수 있는 사람도 있어요.

- 어쨌건 이름이 뭐였죠? 핑핑이, 아니면 팽팽이? 저 이거 못 들으면 오늘 잠 못 자요.

- ……핑핑이.

결국은 대답해 줄 거면서 뭘.

비로소 후련해진 나는 들려오는 웨이펑후의 말에 귀를 기울였다.

「그 누구도 예상치 못한 일이었소.」

쓰촨성은 광활한 면적과 수천만의 인구를 보유한 거대한 성.

그리고 이 모든 일은 쓰촨성에 존재하는 20여 개 행정 구역 중 하나, 난충시의 가오핑구에서 시작되었다.

「알다시피 본국에 존재하는 게이트의 숫자는 타국과 비교하면 열 배 이상 많소. 때문에 대격변 당시 가장 큰 피해를 입었던 국가 중 하나였고, 그만큼 철저하게 관리하고 있었지.」

하지만 사람의 힘으로 천재지변까지 제어할 수는 없었고, 몬스터 웨이브는 천재지변보다 더한 재앙이었다.

「가오핑구에서 마력 수치가 급등했다는 연락을 받은 건, 첫 징후가 나타난 지 정확히 13분이 지난 후였소. 그리고 쓰촨성에 주둔 중이던 공안무력부장 레이페이가 휘하 헌터들을 이끌고 현장에 도착했을 때는…… 모든 것이 늦은 후였지.」

“레이페이?”

낯선 이름. 그러나 어째서일까, 문득 떠오르는 기억이 있었다.

‘출발하기 전, 길드 하우스에서 최 팀장이 보여 줬던 그 영상.’

아직도 생생하다. 홀로그램이 비춘 아비규환의 도시와 헌터들의 선두에서 몬스터들을 베어 가던 한 남자의 모습이.

그의 무기에는 눈이 부실 만큼 찬란한 오라가 맺혀 있었다.

“본 적이 있는 것 같습니다. 혹시 보내 주신 영상에 나왔던 그……?”

「그렇소.」

잠시 머뭇거리던 웨이펑후가 옅은 한숨과 함께 입을 열었다.

「본국이 보유한 S급 헌터 중 한 명이었소. 물론 두 선생께서는 모르시겠지만.」

모를 거라고?

S급 헌터는 전 세계를 통틀어도 스무 명밖에 되지 않는 절대 강자들.

그들이 누리는 유명세와 지위는 무림의 초절정 고수가 가지는 그것보다 훨씬 크고 강하다.

인터넷, 뉴스, SNS가 그들의 발판이고 마이크와 카메라는 그림자처럼 따라붙는다.

무림인을 향한 양민들의 시선이 경계심 반, 호기심 반이라면 현대인들에게 헌터는 그저 선망의 대상이다. 그야말로 세계의 유명인인 것이다.

‘그런데 그런 S급 헌터를 우리가 모른다고?’

웨이펑후는 에둘러 말했지만, 그 말에 담긴 뜻을 알아듣기에는 충분했다.

나와 최 팀장의 시선이 허공에서 부딪쳤다. 이 순간, 우리는 같은 생각을 떠올리고 있었다.

‘드러나지 않은 S급 헌터.’

아니, 정확히 말하자면 중국 정부가 의도적으로 감춘 S급 헌터라고 하는 게 맞겠다.

‘이런 건 소문으로만 들었는데. 사실이었나?’

S급 헌터는 한 국가의 얼굴이나 다름없는 존재.

그러나 얕보이지 않기 위해 안간힘을 쓰는 약자와는 달리, 강자는 오히려 발톱을 감춘다.

이미 두 명의 S급 헌터를 보유하고 있다고 알려진 중국은 모든 힘을 드러내고 싶지 않았던 게 분명했다.

어쩌면 중국뿐만 아니라, 세계 유수의 강대국들도 마찬가지일 것이다.

‘거 참. 대격변을 겪고서도 이런 눈치싸움이라니.’

한심하기도 했고, 한편으로는 이해가 될 것 같기도 하다. 외교, 정치. 내가 알 수 없었던 세상의 진실을 조금이나마 엿본 것 같아 기분이 묘했다.

그리고 그런 나와 달리, 최 팀장은 보다 더 예리한 사람이었다.

「귀국이 보유한 S급 헌터 중 한 명‘이었다’는 건, 과거형으로 들리는군요.」

웨이펑후가 참담한 얼굴로 대답했다.

「……처음 몬스터 웨이브가 일어났던 일주일 전, 레이페이는 실종되었소. 그가 지휘하던 공안무력부의 헌터들과 함께.」

「실종이 확실합니까? 혹시…….」

「죽음은 확인하지 못했소. 그 영상을 마지막으로 리치. 아니지, 아크 리치라 불린 그 몬스터가 마력으로 모든 통신과 감시를 차단했으니까.」

나와 최 팀장은 동시에 침음성을 흘렸다. 우리의 반응에 웨이펑후가 갈라진 목소리로 물었다.

「선생들도 레이페이가 죽었다고 생각하시오?」

“음.”

“어…….”

실종. 그것도 일주일 전에 그 아비규환 속에서 실종되었다면 이미 결말은 정해져 있는 것이나 다름없다.

최 팀장의 눈짓에 나는 조심스럽게 입을 열었다.

“그, 뭐냐. 사람 일은 어떻게 될지 모르는 것이지만…….”

「다른 전문가들은 백 퍼센트 죽었을 거라 하더군. 천하에 쓸모없는 허풍선이들 같으니.」

왜 그래. 진짜 전문가 맞는 것 같은데.

저 상황에서 살아 있다고 장담하는 놈이 있으면 당장 잘라야 한다. 그게 엄연한 사실이니까.

「하지만 내 생각은 다르오. 레이페이, 그 아이는 반드시 살아 있을 거요.」

“저도 그러길 바랍니다만, 아무래도 현실적으로 봤을 때…….”

「하나뿐인 외조카요. 어릴 적부터 병약했던 내 누이는 산고를 이기지 못하고 세상을 떠났고, 젖도 못 뗀 핏덩이를 내가 지금까지 친자식처럼 키웠지.」

“예?”

아니, 외조카라니. 친자식처럼 키웠다니. 이게 뭔 소리야.

석상처럼 굳어 버린 내게 웨이펑후가 축축해진 눈동자로 물었다.

「그런데 뭐라 하려고 했소? 현실적으로 봤을 때, 그 뒤에 말이오.」

시벌, 이건 역대급 위기다.

순간 말문이 턱 막혔던 나는 간신히 목소리를 쥐어짜 냈다.

“그, 현실적으로 봤을 때. 살아 있을 확률도 아주 없진 않다고 말씀을 드리려고 한 건데요.”

「그렇소? 그게 사실이오?」

“아, 예. 하지만 그 확률이라는 게 매우 희박…….”

「고맙소, 진 선생!」

“아니, 장군님. 대장님. 수령님. 잠시만 고정하시고 제 말을 좀 더…….”

덥석!

틀렸다. 웨이펑후는 이미 내 말을 듣고 있지 않았다. 그 대신 눈물이 그렁그렁 맺힌 눈동자로 내 손을 감싸 쥐었다.

「한 가지 부탁해도 되겠소?」

그 부탁, 안 했으면 좋겠는데.

간절한 내 바람과는 달리, 결국 몇 초 후 예상했던 한 마디가 가슴을 파고들었다.

「혹시 나중에 진 선생께서 그 아이를 만난다면 데려와 주실 수 있소?」

“…….”

「내 이리 부탁하리다.」

간절하게 부탁하는 그의 어깨너머로 최 팀장이 고개를 젓는 것이 보인다.

차라리 처음부터 단호하게 대답했다면 어땠을까. 후회했지만 이미 늦었다.

결국 내가 할 수 있는 대답은 하나뿐이었다.

“그렇게 하겠습니다. 하지만…….”

「진 선생.」

“네?”

「굳이 말하지 않아도 되오. 이미 각오하고 있는 일이니.」

“……!”

소매로 눈가를 훔친 웨이펑후는 혈육의 안위를 걱정하는 장년인이 아닌, 중앙군사위원회 국방부장으로 돌아와 있었다.

「이것으로 충분하오. 누구도 선뜻 나서 주질 않았는데, 진 선생이 약속해 주었으니 안심이오.」

“저도 장담할 수는 없습니다.”

「내게 필요한 건 누군가의 호언장담이 아니었소. 실낱같은 희망이었지.」

웨이펑후가 작게 읊조린 그때, 붕 뜨는 부유감과 함께 기체가 지상을 향해 미끄러졌다.

창밖, 짙은 어둠에 휩싸인 그곳에 험악한 산세와 쉴 새 없이 움직이는 불빛, 그리고 군용차량이 보인다.

「도착한 것 같군.」

뭔가에 사로잡힌 사람처럼, 창밖의 풍경을 뚫어져라 바라보던 내가 물었다.

“여기가 어딥니까?”

「임시 작전 본부요.」

“아뇨. 그걸 물어본 게 아닙니다.”

「음?」

“산. 저 산이 왠지 모르게 낯익은 기분이라서요.”

「그럴 리가. 진 선생께선 본국에 입국한 적이 없는 것으로 아는데…… 아, 혹시 사진으로 본 것 아니오?」

“사진이요?”

「유네스코에서 지정한 세계문화유산이니 충분히 가능한 일이지.」

웨이펑후가 옅은 웃음과 함께 말을 이었다.

「임시 작전 본부. 청성산(靑城山)에 온 것을 환영하오.」
```

## Final English reading copy

```markdown
# Chapter 383

The jet Wei Fenghu had prepared looked quite different from what I had imagined.

*It’s spacious. And fancy.*

Through the slightly open cabin door, I could see a luxurious table and what people usually called a chairman’s chair.

Team Leader Choi, who was standing beside me, informed us that the business jet we were looking at cost nearly one hundred billion won per plane, then added,

“Never thought I’d see an aircraft used for state guests here.”

“It is only natural. The two of you are state guests of our country.”

“Ah.”

“Thanks to you, we were able to save countless soldiers and Hunters. None of us—not even me—will ever forget the help you gave us today.”

“…Ah, yes.”

I would have preferred it if they dealt with the fine dust and historical distortions first.

Still, I boarded the aircraft while secretly hoping China was a more conscientious country than I knew.

The waiting pilot saluted us—or, more precisely, Wei Fenghu—with crisp, disciplined movements.

“You have arrived, Comrade Minister of National Defense.”

“How are the preparations?”

“All escort aircraft, including this one, have completed their preparations. We await only your order.”

I had wondered what he meant by “escort,” but then I saw five fighter jets on the runway outside the window. Their sleek, curved bodies flashed their lights as though signaling us.

*What the hell are those?*

I had only ever seen things like that in war movies. Were we about to go off and fight a battle right now?

When Wei Fenghu saw my eyes widen, he spoke.

“It has not yet been properly announced to the outside world…but as you know, Sichuan Province is currently in a state of war. Magical interference with communications and attacks by flying monsters are occurring frequently, so an escort is essential for safety.”

“Is that really true?”

The situation was more serious than I had expected.

The Wyverns had only attacked us in passing while they were raiding Chengdu International Airport, but if this was happening throughout Sichuan Province, that changed things completely.

“If only I were lying.”

Perhaps merely thinking about the current situation exhausted him. Wei Fenghu, who seemed to have aged considerably in a short time, leaned back into the soft seat.

“It seems we must part ways here. We will meet again soon, Senior Colonel Shao Shen.”

Unlike us, one person had not boarded the aircraft. Shao Shen stood at attention and saluted.

“Yes. I will join you after completing my mission as quickly as possible, Comrade Minister of National Defense. And you two gentlemen.”

“Good. I have high expectations.”

Perhaps because he had achieved such impressive accomplishments, a pleased smile passed across Wei Fenghu’s lips as he looked at the promising young Hunter.

Team Leader Choi substituted a respectful bow for a farewell, while I waved.

“See you next time. You fought really well today.”

It had only been one sentence.

But the moment Shao Shen heard my words, his eyes grew as wide as serving trays. His body trembled as though he had been electrocuted, and then he shouted at the top of his lungs.

“Th-Thank you! I will devote myself to every task with the utmost loyalty,[^1] so that you never have cause to be disappointed in me, Mr. Jin!”

“…No need to go that far.”

“May your august self remain safe! Loooyalty!”

“‘August self’? What are you—”

Whack!

“Ugh!”

“…”

That seemed like a textbook example of poor judgment.

He had saluted with such force that the edge of his hand had struck his own eyebrow.

I was staring at Shao Shen as he clenched his teeth and endured the pain when the entrance closed, and the business jet carrying us began to take off.

“That guy is, well, how should I put it… His character is pretty unique.”

At my dissatisfied comment, Wei Fenghu let out a quiet laugh.

“You can hardly blame him. He received praise from his idol.”

“Excuse me?”

“There are many young Hunters in our country who admire you, Mr. Jin. That young man is no exception.”

*What the hell? Was I a Korean Wave star?*

Come to think of it, for a four-star general reputed to be able to knock birds out of the sky with a single finger, this man seemed unusually interested in his subordinates.

Or maybe Shao Shen was simply that promising.

Ah, but…

—Team Leader. How important is the Minister of National Defense under the Central Military Commission, exactly? I’m not very familiar with the structure over here.

Team Leader Choi flinched at my Sound Transmission and answered through Message Magic.

—If you compare it to our country, he is the Minister of National Defense. Of course, this is China, and Wei Fenghu is the current Chairman’s right-hand man, so his power is considerably greater.

—Ah.

*He’s not that different from me. I’m the Minister of gukbap.[^2]*

One special serving of sundae-guk was enough to handle three bowls of rice.

Of course, Wei Fenghu could probably erase three cities with a single pointed finger.

And now, that powerful figure of the People’s Republic of China was leaning his upper body toward us and asking,

“It seems we have many things to discuss during the journey. Would you not agree?”

Team Leader Choi and I nodded solemnly and opened our mouths.

“Of course. First, I would like to ask exactly what is happening in Sichuan—”

“But do you happen to have any boiled eggs and soda? I’m hungry after fighting so hard.”

“…”

“…”

Apparently, they did not.

“We do.”

“…”

“…”

They did.

* * *

The People’s Republic of China.

As one could tell from the country’s formal name, these imposing people of the continent still held socialism as their national ideology.

About twenty years ago, the Chairman of that time died during the Great Cataclysm after laying a firm foundation for dictatorship through lifelong rule. Power was transferred to a much more moderate government, but the core remained unchanged.

—What was the dead Chairman’s name again? Pingping? Paengpaeng?

Team Leader Choi, who had been chiming in as Wei Fenghu spoke, silently moved his lips. His poker face was astonishing.

—Just in case you were wondering, saying something like that here would get you into serious trouble.

—That’s why I’m using Sound Transmission—no, Message Magic.

—I’m telling you to be careful. Some outstanding mages of A rank or higher can eavesdrop on Message Magic.

—Anyway, what was his name? Pingping or Paengpaeng? If I don’t find out, I won’t be able to sleep tonight.

—…Pingping.

*You were going to answer me in the end anyway.*

Now that I was finally satisfied, I listened closely to Wei Fenghu’s words.

“No one could have predicted what happened.”

Sichuan Province was an enormous region with a vast area and a population of tens of millions.

And all of this had begun in Gaoping District of Nanchong City, one of the roughly twenty administrative divisions in Sichuan Province.

“As you know, our country has more than ten times as many Gates as other countries. Because of that, we were one of the nations hit hardest during the Great Cataclysm, and we have managed them with corresponding rigor ever since.”

But human power could not control even natural disasters, and the Monster Wave was a calamity far worse than any natural disaster.

“We received word that the mana levels in Gaoping District had suddenly spiked exactly thirteen minutes after the first signs appeared. And by the time Lei Fei, head of the Public Security Armed Forces Department stationed in Sichuan Province, arrived at the scene with the Hunters under his command…everything was already too late.”

“Lei Fei?”

The name was unfamiliar. And yet, for some reason, a memory suddenly came to me.

*That video Team Leader Choi showed me at the Guild house before we left.*

I still remembered it clearly. A city thrown into chaos beneath the light of a hologram, and a man cutting down monsters at the head of the Hunters.

An aura bright enough to blind me had gathered around his weapon.

“I think I’ve seen him before. Is he the one who appeared in the video you sent us…?”

“That is correct.”

Wei Fenghu hesitated for a moment before speaking with a faint sigh.

“He was one of our country’s S-rank Hunters. Of course, the two of you would not have known about him.”

*We wouldn’t know?*

There were only twenty S-rank Hunters in the entire world. They were absolute powerhouses.

The fame and status they enjoyed were far greater than those of even a Supreme Peak master in the Murim.

The internet, news, and social media were their platforms, while microphones and cameras followed them like shadows.

If the common people of the Murim looked at martial artists with half wariness and half curiosity, modern people simply admired Hunters. They were celebrities known throughout the world.

*But we’re supposed to not know an S-rank Hunter like that?*

Wei Fenghu had spoken indirectly, but it was enough for me to understand what he meant.

Team Leader Choi’s gaze met mine in midair. At that moment, we were thinking the same thing.

*An undisclosed S-rank Hunter.*

No, to be precise, an S-rank Hunter deliberately concealed by the Chinese government.

*I’d only heard rumors about things like this. So they were true?*

An S-rank Hunter was practically the face of a nation.

But unlike the weak, who struggled desperately to avoid being underestimated, the strong concealed their claws.

China was already known to possess two S-rank Hunters. It was obvious that they had not wanted to reveal all their strength.

*Maybe the other great powers of the world were the same.*

*Good grief. Even after surviving the Great Cataclysm, they’re still playing this kind of game of nerves.*

It was pathetic, but at the same time, I thought I could understand it. Diplomacy. Politics. I felt as though I had caught a glimpse of the truths of a world I had never known, and the feeling was strange.

Unlike me, however, Team Leader Choi was sharper.

“When you say he ‘was’ one of the S-rank Hunters your country possesses, I take it you are speaking in the past tense.”

Wei Fenghu answered with a devastated expression.

“…A week ago, when the first Monster Wave began, Lei Fei disappeared. Along with the Hunters of the Public Security Armed Forces Department under his command.”

“Are you certain he is missing? Perhaps…”

“We could not confirm his death. After that video was recorded, the monster known as the Lich—no, the Arch Lich—blocked all communications and surveillance with mana.”

Team Leader Choi and I both groaned.

At our reaction, Wei Fenghu asked in a hoarse voice,

“Do you two also believe that Lei Fei is dead?”

“Hmm.”

“Uh…”

If someone had disappeared in that chaos a week ago, the outcome was practically decided already.

At Team Leader Choi’s glance, I cautiously opened my mouth.

“Well, you never know what can happen to someone, but…”

“The other experts said he was one hundred percent dead. Useless windbags, the lot of them.”

*Why are you saying that? They seem like genuine experts.*

If anyone claimed he was alive in that situation, they should be fired immediately. That was simply a fact.

“But I disagree. Lei Fei—my boy—is certainly alive.”

“I hope so too, but realistically speaking…”

“He is my only nephew. My sister had been sickly since childhood. She died in childbirth, unable to survive the ordeal, and I raised that tiny baby, who had not even been weaned, as if he were my own son.”

“Excuse me?”

*Your nephew? You raised him as your own son? What is this supposed to mean?*

As I sat frozen like a statue, Wei Fenghu asked me with damp eyes,

“What were you about to say? After ‘realistically speaking.’”

*Crap. This is an all-time crisis.*

My words caught in my throat. I barely managed to squeeze out a voice.

“I was going to say that, realistically speaking, there is still a chance he could be alive.”

“Is that so? Is that really true?”

“Yes, but that chance is extremely slim—”

“Thank you, Mr. Jin!”

“No, General. Commander. Supreme Leader. Please hold on for a moment and let me finish…”

Grab!

It was too late. Wei Fenghu was no longer listening to me. Instead, he clasped my hand in both of his, his eyes brimming with tears.

“May I ask you for one favor?”

*I really wish you wouldn’t.*

Contrary to my desperate hopes, a few seconds later, the one sentence I had expected pierced my heart.

“If you happen to meet that boy someday, could you bring him back to me?”

“…”

“I beg you.”

Over Wei Fenghu’s shoulder, I saw Team Leader Choi shaking his head.

What if I had answered firmly from the very beginning? I regretted it, but it was already too late.

In the end, there was only one answer I could give.

“I will. But…”

“Mr. Jin.”

“Yes?”

“You do not need to say it. I am already prepared for what may happen.”

“…”

Wei Fenghu wiped the corner of his eye with his sleeve. He had returned from a middle-aged man worried about the safety of his blood relative to the Minister of National Defense under the Central Military Commission.

“This is enough. No one was willing to step forward, but you have given me your word, Mr. Jin. I am relieved.”

“I cannot guarantee anything.”

“I did not need someone’s boastful guarantee. What I needed was a thread of hope.”

Just as Wei Fenghu murmured those words, the aircraft began to descend, accompanied by a sudden sensation of floating.

Outside the window, beneath a blanket of deep darkness, I could see rugged mountain ridges, lights moving without pause, and military vehicles.

“It seems we have arrived.”

I had been staring fixedly out the window as though possessed by something. Then I asked,

“Where are we?”

“A temporary operations headquarters.”

“No. That is not what I meant.”

“Hmm?”

“For some reason, that mountain feels strangely familiar.”

“That cannot be. As far as I know, you have never entered our country… Ah, could you have seen it in a photograph?”

“A photograph?”

“It is a UNESCO-designated World Cultural Heritage Site, so that would certainly be possible.”

With a faint smile, Wei Fenghu continued,

“Temporary operations headquarters. Welcome to Mount Qingcheng.”[^3]

[^1]: A self-deprecating Korean idiom meaning to offer one’s utmost loyal service, literally “the labor of a dog or horse.”

[^2]: *Gukbap* is rice served in hot soup; here, Taekyung is riffing on the similar sound of *gukbangbu*, the Ministry of National Defense.

[^3]: Mount Qingcheng is a UNESCO World Heritage site associated with the Qingcheng Taoist tradition.
```
