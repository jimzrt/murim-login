<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1153.txt",
      "sha256": "f25866137448b99b9af0b637b76e1120540a06d7706ded8a22f69b5925551c61",
      "bytes": 11325
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1834097dfcd214d2b71f04e3efd9373eb4d8fc1a1e5d44484bcf4b7817a541c1",
      "bytes": 1124
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0235b29aa796a689ced157ef803ab836ad2426783b12138adbefa4121422f8ad",
      "bytes": 246740
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "b273b20c6a838f44a53b5d05ecbd4c553fdd966a4097cda76d6c467ffd9a240a",
      "bytes": 844
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "4c87b03c5034909056bd9e1718da83acc7b20f3be53bbf8209532947e7f6c9e3",
      "bytes": 777
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "189e768ddb3210f7665e66def7245a65033c59fc0e4a3e4405d13bdcc90b7397",
      "bytes": 867
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "85939be45ec158d6cb00938a0d549ad4e2ce77d13403ba8123f26091090ed734",
      "bytes": 796
    },
    {
      "path": "characters/Pill Physician.md",
      "sha256": "6847935717b5c90c0ca73644e73c9c249a184ec0135cb5842c5b1b5791630592",
      "bytes": 554
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "595d0dc2eb7867ad8ab576966d6b2d210f9da6690172006796dbd9280f3be920",
      "bytes": 292837
    }
  ],
  "estimated_tokens": 8211
}
-->

# Durable State Update — Chapter 1153

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 1153. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1153. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 1153,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1153,
    "continuity_sources": [1153],
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
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "Vladimir, powered by a Magic Gem, destroyed Moscow; Morgoth survived the blast and created a Dragon Lair over the ruins.",
    "Morgoth’s attack on Moscow was broadcast worldwide; the narrator hears a minimum death estimate of twenty million and no signs of life.",
    "Pie Chen, the narrator’s friend and an S-rank Hunter from Hong Kong, died a week earlier fighting Morgoth rather than joining him.",
    "Chuck Hagel survived because of Pie Chen’s sacrifice; he has only his right arm left and regrets that she died in his place.",
    "The United States President announced that the returning savior has come back; the narrator vows to prevent further sacrifices and intends to face Morgoth."
  ],
  "continuity_sources": [
    1151,
    1152
  ],
  "open_questions": [
    "How will the nations respond to Morgoth’s destruction of Moscow?",
    "Can the narrator defeat Morgoth?"
  ],
  "safe_through": 1152,
  "temporary_decisions": [
    "Render 블라디미르 as “Vladimir,” 흑룡공 as “Black Dragon Duke,” and 파이 첸 as “Pie Chen.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 천태민    | **Cheon Taemin**  |
| 무신     | **Martial God**               | —              |
| 상태               | **Status**                     |
| 칭호               | **Title**                      |
| 로그아웃             | **Logout**                     |
| 지능               | **Intelligence**               |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 대사      | **Master** for a senior Buddhist monk                           |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 환의 | **Pill Physician** | Title of the current Family Head of the Seongsu Jang Family. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 대통령 | **President** | Title for Korea's head of state. |
| 도람프 | **Doramp** | Parodic name for the U.S. president in a forum headline. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 모스크바 | **Moscow** | Russian city used in Taekyung's modern-world comparison. |
| 펜타곤 | **Pentagon** | Headquarters of the United States Department of Defense and source of intelligence about terrorist experiments. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 스카이 | **Sky** | American epithet for Cheon Taemin. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 미합중국 | **United States** | Formal Korean reference used during the Defense Minister's imperialist rant. |
| 적도 | **Red Blade** | Named blade that shatters in Taekyung’s flames. |
| 흑룡공 | **Black Dragon Duke** | Title in Morgoth's System announcement. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1139
- **Aliases:** None
- **Role:** Deceased young-seeming high-ranking Dark Heaven figure who claimed command of its army after killing the Grand Mage.
- **Personality:** Cunning and controlling, he trusts his overwhelming power and relishes opponents who survive and resist him; he resents the Lord of Heaven’s attention to Taekyung and rationalizes his intended murder as loyalty, yet believes his choice is right.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He served the Lord of Heaven, killed the Grand Mage, and died after Jin Taekyung defeated him; at death, he recognized that the Lord had never valued his loyalty.

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 1144
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Ares Guild Master and humanity's greatest Hunter, the Slayer who defeated the Demon King and created the first Mana Cultivation Method during the Great Cataclysm; after more than twenty years in seclusion, he remains unconscious in a secret area within Area A.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 1149
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger was a Demon Realm being capable of regenerating in new bodies and was erased by Jin Taekyung.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** It speaks with theatrical, grandiose confidence, taunting opponents in polished, self-important phrasing.
- **Relationships:** It claims to have served Demon King Asmodeus as its master and acted on his order, regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 1144
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one; Taekyung now suspects The Helper was the Martial God and that the Martial God was Cheon Taemin, though both identities remain unconfirmed.

### Pill Physician.md

# Pill Physician (환의)

- **Safe through:** Chapter 995
- **Aliases:** None
- **Role:** Current Family Head of the Seongsu Jang Family in Shandong, who personally placed and signed the Thousand-Year Snow Ginseng in the casket entrusted to the Yongbong Escort Bureau.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** The Pill Physician heads the Seongsu Jang Family, a prestigious medical family in Shandong.

## Korean source

```text
＃1153화



인간은 누구나 죽는다.

세상 그 누구도 따라올 수 없는 막대한 부와 명예를 쌓아도, 초인이라 칭해질 만큼 강인한 육체와 정신을 지녔더라도 죽음의 그림자는 결코 피하지 못한다.

그렇기에 나는, 우리는 가까웠던 동료들의 비보(悲報)를 힘겹게나마 받아들일 수밖에 없었다.

아니, 그래야만 했다.

순간의 감정에 휩쓸리기에는, 당장 눈앞에 닥친 현실이 너무나도 참혹했으니까.

“……이상으로 회의를 마칩니다.”

발표자의 지친 목소리와 함께 불이 켜졌지만, 주위를 짓누르고 있던 무거운 정적은 쉽사리 흩어지지 않았다.

회의 내내 침묵하던 한 사람이 입을 열기 전까지는.

“휴식은 중요하죠. 이럴 때일수록 특히. 그렇지 않습니까?”

별것 아닌 한마디였지만, 그 안에 담겨 있는 속뜻을 이해하지 못한 사람은 없었다.

그 정도의 눈치도 없었다면, 애당초 지금 이 자리에 동석하는 것조차 불가능했을 테니.

“이제야 조금 숨통이 트이는군요.”

비로소 한산해진 회의실 내부, 한 구석에 마련된 커피포트 앞으로 다가간 중년인이 나를 향해 눈짓했다.

“한 잔 드릴까요? 미스터 진.”

온통 기름지고 헝클어진 머리카락과 진한 다크서클.

피로에 찌들 대로 찌든 직장인의 모습을 한 그의 제안에 나는 고개를 저었다.

“괜찮습니다. 대통…….”

“편하게 도니라고 부르셔도 됩니다.”

“예, 그러죠. 도니.”

내 담담한 승낙에 미합중국의 57대 대통령, 도널드 도람프 주니어가 빙긋 웃었다.

물론 그마저도 짧게 떠올랐다가 흔적도 없이 사라진 억지웃음에 불과했지만.

‘그럴 수밖에.’

나도 모르게 시선이 향한 곳에는, 아직 꺼지지 않은 홀로그램이 허공에 떠올라 있었다.

닳고 닳은 정치인조차 웃을 수 없게 만드는, 파멸적인 피해 수치와 함께.

“백악관에서 처음으로 관련 보고를 받은 순간 생각했죠. 꿈인가?”

포션이 다량 첨가된 커피를 단숨에 들이켠 그가 말을 이었다.

“사실, 지금까지도 비슷한 생각을 합니다. 이 모든 게 빌어먹을 악몽이길 바라면서요.”

그러나 현실은, 보고서에 적힌 수치는 꺾이긴커녕 나날이 솟구쳤다.

경(京) 단위의 재산 피해와 수천만의 사상자, 동시에 그 이상의 난민이 발생했으며 전 세계는 패닉에 빠졌다.

“그래서 최대한 빨리 알릴 수밖에 없었습니다. 당신이 돌아왔다는 사실을.”

그의 말처럼, 국제 사회는 신속하게 움직였다.

상임이사국을 필두로 한 UN 안보리는 즉각 긴급 성명을 발표했고, 중동에서 행적이 묘연해진 내가 귀환 소식은 전 세계에 퍼졌다.

당사자인 내가 바로 이곳, 펜타곤(Pentagon)에 도착하기도 전에.

“관련 논의 때 섣부른 발표라는 의견도 있었지만, 당시의 상황에서는 어쩔 수 없었습니다. 혹시 저희가 잘못된 판단을…….”

“아닙니다. 전혀요.”

나는 사과하는 대통령에게 손을 내저었다.

이제 와서 수습하기에는 이미 엎질러진 물이라서?

물론 그것도 어느 정도는 맞다.

하지만 내가 귀환했다는 소식이 알려지지 않았다면, 사람들은 더더욱 걷잡을 수 없는 소용돌이 속으로 빠졌을 것이다.

재앙이란 본래 공포와 혼란 속에서 잉태되는 법이니까.

게다가 그 재앙의 씨앗은 이미 꽃을 피우고 있었다.

흑룡공 모르고스라는, 사상 초유의 몬스터로 인하여.

“진, 저는 지난 12년간 미합중국의 대통령으로서 수많은 중대사를 처리해 왔습니다. 하지만 그중에서도 가장 최우선적이자 중요한 사안은 따로 있었죠.”

나는 그가 뭐라 말을 잇기도 전에 정답을 알고 있었다.

마왕 아스모데우스가 이 세상에 강림한 이후부터, 전 세계의 모든 나라가 같은 문제에 직면해 있었으니까.

“몬스터와의 전쟁.”

혼잣말처럼 뇌까린 한마디에 도널드 대통령이 고개를 끄덕였다.

“맞습니다. 대격변 이후에도 사라지지 않은 게이트(Gate)에 관한 문제, 더 나아가 혹시 모를 제2의 대격변에 관한 대비책 수립이 우리의 최우선 과제였습니다.”

텅 빈 커피잔을 말없이 내려다보던 그가, 힘없이 덧붙였다.

“그리고 그 대비책은 실패했습니다. 아니 정확히는…….”

“대비하고 있었음에도 상대할 수 없을 정도로 강한 놈이 나타난 거겠죠. 이해합니다.”

내가 본 모르고스는 그만큼 강대한 존재였다.

설령 그것이 모든 전력이 아니더라도, 영상 속에 비친 놈의 힘은 대격변 당시부터 지금까지 등장한 그 어떤 네임드 몬스터도 비견될 수 없을 정도였다.

단 한 존재.

재앙을 넘어 종말이라고까지 불리었던 절대악, 마왕 아스모데우스를 제외한 그 누구도.

게다가…….

“그 대비책의 핵심은 결국 ‘그’가 있어야 비로소 완성되는 것이었겠죠. 아닙니까?”

도널드 대통령이 무겁게 고개를 끄덕였다.

“그렇습니다. 스카이(Sky)가 의식불명 상태에 빠진 이후부터 우리의 계획은 힘을 잃었습니다.”

스카이, 천태민.

2차 세계대전을 종식시킨 것이 두 발의 원자폭탄이었다면, 그는 대격변을 온몸으로 헤쳐 나가며 모든 인류를 구원했다.

‘그래, 무신(武神)이 그랬듯이.’

혀끝에 맴도는 말을 삼킨 그때, 도널드 대통령이 말을 이었다.

“하지만 우리의 문제는 스카이의 부재뿐만이 아닙니다. 모르고스의 무력은 그 자체만으로도 재앙이나 다름없지만…… 놈은 그 어떤 몬스터와도 비교할 수 없는 특별함을 지니고 있어요.”

이번에도 역시, 나는 답을 알고 있었다.

“외교.”

“역시, 당신도 느끼고 있었군요.”

“몬스터의 생리에 대해서는 지긋지긋할 정도로 겪어 봤으니까요.”

살면서 먹은 끼니의 숫자를 외우지 못하는 것처럼, 나 역시 F급 헌터 시절부터 셀 수 없을 만큼 많은 몬스터를 쓰러트려 왔다.

그렇기에 잘 안다.

지능의 높고 낮음, 힘의 우위를 떠나 몬스터란 존재는 기본적으로 살육의 본성을 타고났다는 것을.

‘아니, 오히려 강하면 강할수록 더 짓밟으려는 성향이 강했지. 압도적인 힘으로 모든 것을 해결하려 했으니까.’

물론 그중에도 예외는 있었다.

지금 이 자리에 없는 스켈레톤 킹이 그랬고, 모르고스 소환의 단초가 되었던 도플갱어는 오래전부터 인간 사회에 녹아들어 암약하기까지 했다.

그러나 모르고스는 궤가 다르다.

단순한 기만이나 속임수 따위가 아니라 진심으로 항복을 제안하고, 만약 그에 응한다면 확실한 생존을 보장한다.

‘약속을 지키는 몬스터라니.’

그리고 이와 같은 놈의 행보는, 어느 때보다 큰 분열을 일으키고 있었다.

“이미 23개국이 모르고스에게 항복했습니다. 가장 큰 타격을 입은 아랍 연맹(LAS)에 더해, 남미의 주요 국가 일부가 저항을 포기한 거죠.”

“중동 지역은 사실상의 함락이라고 칠 수 있겠지만, 남미까지요?”

“모스크바 사건의 영향이 컸습니다. 최대한 통제해 보려고 노력했지만, 정보가 퍼지는 걸 막을 수가 없었어요.”

재앙은 공포를 낳고, 공포는 균열로 이어진다.

생존이라는 가장 강력한 욕구 앞에서, 사람들은 하나둘씩 무너져 내리고 있었다.

“과거 대격변 초기에도 비슷한 상황이 벌어졌다지만, 그때와는 다릅니다. 모두가 동요하고 있습니다.”

인류가 대격변을 승리로 마무리 지을 수 있었던 이유는 생각보다 간단하다.

단합했기 때문이다.

아이러니하게도 적이었던 아스모데우스가 그것을 가능케 했다.

놈은 실로 마왕이라는 칭호에 걸맞는 존재였다.

저항하는 자도, 항복하는 자도 죽였다.

대도시를 불태우고 산과 바다를 뒤엎었다.

타협? 약속?

놈에게는 어느 날 집에서 발견된 바퀴벌레가 공생을 대가로 복종을 맹세하는 것이나 다름없었다.

그렇게 인류는 한 마음 한뜻으로 온 힘을 다해 맞서 싸울 수 있었다.

다행히 그들에게는 천태민이라는 구원자가 존재했고, 선택지 따위는 존재하지 않았으니.

‘하지만 모르고스는 약속을 지켰지. 아스모데우스와는 다르게.’

인간의 모습으로, 인간들의 방식을 따른다.

저항하는 자에게는 처참한 파괴와 죽음을, 투항하는 자에게는 확실한 생존을 보장한다.

마치, 중세 시대의 잔혹한 정복 군주처럼.

“만약 당신이 때맞춰 나타나지 않았더라면, 저 역시 지금쯤 빌어먹을 항복 문서에 서명하고 있었을지도 모르겠군요.”

도널드 대통령은 씁쓸하게 웃었지만, 나는 머릿속을 헤집는 생각들로 인해 웃지 못했다.

‘때맞춰 왔다고? 내가?’

모르겠다.

만약 내가 혈주(血主)를 쓰러트린 후 정신을 잃지 않았다면 어땠을지.

하루라도 일찍 깨어났다면, 아니 단 몇 시간이라도 로그아웃을 시도했다면…….

투둑.

어느새 점점이 떨어지는 핏방울.

나도 모르게 꽉 움켜쥔 주먹 사이로 흐르는 핏물에, 잠시 침묵하던 도널드 대통령이 입을 열었다.

“진, 모두 벌어진 일입니다. 그리고 아무도 당신을 탓하지 않아요. 당신과 달리 우리는 각자의 자리에 있었지만, 그럼에도 모르고스를 막지 못했으니.”

안다.

남들과는 다른 힘을 얻게 된 이후부터 나는 매 순간 몸부림쳐 왔고, 그 결과로 수많은 생명을 지킬 수 있었다.

하지만 그럼에도 불현듯 솟구치는 분노와 자책은 쉽게 사라지지 않는다.

‘아마도, 모든 것이 끝난 후에도 마찬가지겠지.’

사람들은 나를 새 시대의 구원자라고 말하지만, 나 역시 그들처럼 한 명의 인간이다.

가진 것보다 잃어버린 것에 집착하고, 곧 다가올 위험을 두려워하는.

그리고 그 위험은, 생각하는 것 이상으로 가까이에 있다.

“대통령 각하!”

다급한 외침과 함께 회의실로 들어온 비서관의 뒤로, 낯익은 얼굴들이 보였다.

하나같이 딱딱하게 굳어 있는 입매와 가라앉은 눈동자.

주위의 공기가 일순간 얼어붙은 순간, 비서관의 손길에 의해 켜진 홀로그램 영상이 허공에 떠올랐다.

팟.

끊임없이 치직거리는 노이즈 속, 넓은 회의실 내부를 메운 것은 수만 킬로미터 밖의 풍경이었다.

한때 모스크바라 불렸던, 검게 물든 대지 위에 우뚝 선 드래곤 레어가 모두의 시야를 가렸다.
```

## Final English reading copy

```markdown
# Chapter 1153

Everyone dies.

No matter how much wealth and fame a person amasses—more than anyone else in the world—or how strong their body and mind become, until they’re called superhuman, they can never escape the shadow of death.

That was why we had no choice but to accept, however painfully, the tragic news of our close companions’ deaths.

No. We had to.

The reality right in front of us was simply too horrific to give in to our emotions.

“That concludes the briefing.”

The lights came on with the presenter’s exhausted voice, but the heavy silence pressing down on the room didn’t disperse so easily.

Not until someone who had kept silent throughout the meeting finally spoke.

“Rest is important, isn’t it? Especially at a time like this.”

It was a simple remark, but no one failed to understand what lay beneath it.

Anyone that oblivious wouldn’t have been allowed in this room in the first place.

“I can finally breathe a little.”

The conference room had at last emptied out. A middle-aged man walked over to the coffee machine tucked in one corner and glanced at me.

“Would you like a cup, Mr. Jin?”

His hair was greasy and disheveled, and dark circles ringed his eyes.

He looked like an office worker worn down to the bone by exhaustion. I shook my head at his offer.

“No, thank you, Mr. Presi—”

“You can just call me Donny.”

“Sure. Donny.”

At my matter-of-fact reply, Donald Doramp Jr., the fifty-seventh President of the United States, smiled faintly.

Even that was only a forced smile that appeared for a moment before vanishing without a trace.

*Of course it was.*

My eyes drifted to the hologram still hanging in the air—the catastrophic casualty figures enough to rob even a thoroughly jaded politician of a smile.

“The first time I received a report about it at the White House, I thought, ‘Is this a dream?’”

He downed a coffee heavily laced with potions and continued.

“To be honest, I still think the same thing. I keep hoping all of this is one goddamn nightmare.”

But this was reality. The numbers in the reports hadn’t leveled off; they’d climbed higher with every passing day.

Property damage in the tens of quadrillions. Tens of millions dead or injured, and even more refugees. The whole world was in a panic.

“That’s why I had to announce as soon as possible that you’d returned.”

As he said, the international community had moved quickly.

The UN Security Council, led by its permanent members, had immediately issued an emergency statement. News of my return spread around the world after I’d gone missing in the Middle East.

Before I, the person at the center of it all, had even arrived here at the Pentagon.

“Some people thought announcing it during the discussions was premature. But given the circumstances, we had no choice. What if we made the wrong call—”

“No. You didn’t.”

I waved off the President’s apology.

Because it was too late to put the genie back in the bottle now?

That was part of it, of course.

But if the news of my return hadn’t gotten out, people would have been swept into an even more uncontrollable maelstrom.

Disaster, after all, takes root in fear and confusion.

And the seed of that disaster had already blossomed.

All because of an unprecedented monster: Black Dragon Duke Morgoth.

“Jin, I’ve handled countless major crises over the past twelve years as President of the United States. But there’s always been one matter that came before all the others—the most important priority.”

I knew the answer before he could continue.

Ever since Demon King Asmodeus descended upon this world, every country had been facing the same problem.

“The war against monsters.”

Donald nodded at my words, spoken almost under my breath.

“That’s right. The Gates that remained after the Great Cataclysm, and the preparations for a possible second Great Cataclysm—they were our top priorities.”

He stared silently down at his empty coffee cup, then added weakly, “And our preparations failed. Or, more precisely…”

“Something showed up that was too strong for us to handle, even though we were preparing for it. I understand.”

Morgoth was that powerful.

Even if the footage didn’t show all of his strength, what I’d seen onscreen was beyond anything any named monster had displayed from the Great Cataclysm up to now.

There was only one being who could compare.

No one but the absolute evil known as the Demon King Asmodeus—the one called not merely a calamity, but the end of the world.

And besides…

“But your preparations couldn’t be complete without *him* there, could they?”

Donald nodded gravely.

“That’s right. Our plan lost its strength when Sky fell into a coma.”

Sky. Cheon Taemin.

If two atomic bombs had brought World War II to an end, Cheon Taemin had saved all of humanity by weathering the Great Cataclysm with his own body.

*Right. Just as the Martial God did.*

I swallowed the words on the tip of my tongue. Donald continued.

“But Sky’s absence isn’t our only problem. Morgoth’s power is a calamity all on its own…but he has something no other monster can compare to.”

Once again, I knew the answer.

“Diplomacy.”

“So you’ve noticed it too.”

“I’ve dealt with monsters enough to be sick of them.”

I couldn’t remember every meal I’d eaten in my life. In the same way, I’d taken down too many monsters to count, going all the way back to my days as an F-rank Hunter.

So I knew.

No matter how intelligent they were, no matter how strong they were, monsters were born with an instinct to kill.

*If anything, the stronger they were, the more they wanted to crush everything beneath them. They tried to solve everything with overwhelming force.*

Of course, there were exceptions.

The Skeleton King, who wasn’t here, was one. And the Doppelganger, who had helped set Morgoth’s summoning in motion, had long ago infiltrated human society and operated in secret.

But Morgoth was different.

He wasn’t just bluffing or tricking people. He offered surrender in earnest, and if they accepted, he guaranteed their survival.

*A monster that keeps its promises.*

His actions had caused more division than ever before.

“Twenty-three countries have already surrendered to Morgoth. Besides the Arab League, which suffered the heaviest losses, some major South American countries have given up resisting.”

“The Middle East has more or less fallen, but South America too?”

“The Moscow incident had a huge impact. We did everything we could to contain it, but we couldn’t stop the information from spreading.”

Disaster breeds fear, and fear leads to fractures.

Faced with the most powerful desire of all—survival—people were crumbling one after another.

“A similar thing happened early in the Great Cataclysm, but this is different. Everyone’s shaken.”

The reason humanity had managed to bring the Great Cataclysm to an end with a victory was simpler than you might think.

They united.

Ironically, it was their enemy, Asmodeus, who made that possible.

He truly lived up to the title of Demon King.

He killed those who resisted and those who surrendered.

He burned down cities and overturned mountains and seas.

Compromise? Promises?

To him, it was as if a cockroach found in his house one day had sworn to obey him in exchange for living together.

That was how humanity had been able to fight back with all its strength, united in purpose.

Fortunately, they had Cheon Taemin, a savior, and no other choice.

*But Morgoth kept his promises. Unlike Asmodeus.*

He took human form and followed human customs.

For those who resisted, he offered devastating destruction and death. For those who surrendered, he guaranteed survival.

Like a cruel conqueror from the Middle Ages.

“If you hadn’t appeared in time, I might be signing the goddamn surrender documents by now.”

President Doramp gave a bitter smile, but I couldn’t smile. My thoughts were tearing through my head.

*I came in time? Me?*

I didn’t know.

What if I hadn’t lost consciousness after defeating the Blood Lord?

If I’d woken up even a day earlier—or tried to log out just a few hours sooner…

*Drip.*

Blood drops fell, one after another. It was running from between my fingers where I’d clenched my fist without realizing it. After a brief silence, President Doramp spoke.

“Jin, what’s done is done. And nobody blames you. Unlike you, we were all in our own places, and we still couldn’t stop Morgoth.”

I knew.

Ever since I’d gained powers unlike anyone else’s, I’d struggled at every turn. And as a result, I’d saved countless lives.

But the sudden surges of anger and self-blame still refused to fade.

*They probably won’t, even after everything is over.*

People called me the savior of a new age, but I was only human, just like them.

I fixated on what I’d lost instead of what I had, and feared the danger that was coming.

And that danger was closer than I thought.

“Mr. President!”

An aide rushed into the conference room. Behind him were several familiar faces.

Every one of them wore a tight expression, their eyes downcast.

The air froze in an instant. At the aide’s touch, a holographic video sprang into the air.

*Pop.*

Through the constant crackle of static, a landscape tens of thousands of kilometers away filled the vast conference room.

A Dragon Lair rose over the blackened earth once known as Moscow, blocking everyone’s view.
```
