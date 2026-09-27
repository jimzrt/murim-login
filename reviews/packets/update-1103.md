<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1103.txt",
      "sha256": "bc2a5ec368b6bcb700078b4c2049f7c3d5e70797746892baa40308b2ea1988a8",
      "bytes": 12879
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ef650b69705af5cf7e6b631a9c0ecc6047be62b262e2f58e8f56a11440d71902",
      "bytes": 1301
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2195176fcecc1f2d4760ffbc4a2601370e7609089bc148ea8deda43236c266fc",
      "bytes": 244248
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "d933b389e48a63095de59c2c056bb6ca4e41745265879d6d90ffc926d6588027",
      "bytes": 907
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "ccb471d91a6a75335ae1924b4bb86844f686e8916245ad225ed86d10832d5483",
      "bytes": 1120
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5be41e1a7317c270450b7960bff80b657063b2f22c21f72d34afeddaf58a783f",
      "bytes": 760
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ca168b4cbaa079e7e2aebbd6e32ed3582ebf0ebaeb6e161ee00f0f667e9fbc28",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c887039c1c50dfedb69f18fb1637bd99b853291dee0958bb8926bf1d9656bf3f",
      "bytes": 623
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "f1f66865e7eebc1cfde864e1d23bb12e5826d502070f96840f6abd4b76f90b53",
      "bytes": 755
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f15b6bb616e0bd10e582c2c20db1381f3647dfe2374b0b254aed2c21ef827565",
      "bytes": 287948
    }
  ],
  "estimated_tokens": 10014
}
-->

# Durable State Update — Chapter 1103

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
1 and safe_through 1103. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1103. Profile updates may replace only one
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
  "chapter": 1103,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1103,
    "continuity_sources": [1103],
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
    "Dark Heaven and the Potala Palace are attacking Xining; the siege is underway.",
    "The Blood Lord is coordinating pressure across the gates to exhaust the defenders and create an opening.",
    "The Dalai Lama leads roughly ten thousand Potala Palace monks toward the North Gate to attack Jeok Cheongang and avenge the Palace’s ancestral grievance.",
    "The Blood Lord expects allies to arrive by river from the east; a skeletal eagle has signaled their approach.",
    "The Blood Lord privately wants Jin Taekyung dead but conceals this from the Grand Mage and will not defy that person’s will."
  ],
  "continuity_sources": [
    1101,
    1102
  ],
  "open_questions": [
    "Why does the Lord of Heaven want Taekyung, and what does he intend to do with him?",
    "Whom do the Eldest Senior Brother and Elders serve, and what was Mu Song about to reveal?",
    "Who are the allies approaching by river from the east?",
    "Which of Cheongheoja’s Disciples is the hidden Dark Heaven agent, and what did Cheongheoja ask Taekyung to do?"
  ],
  "safe_through": 1102,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 청풍     | **Cheongpung**     |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 소협      | **Young Hero**                                                  |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 무아지경 | **Trance** | State Taekyung briefly enters during the energy digestion. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 일기당천 | **One Against a Thousand** | Title that temporarily increases Taekyung’s attributes and Intimidation when facing many enemies. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 무아 | **No-self** | The brief self-forgetting state the disciple mistakes for a breakthrough. |
| 서녕 | **Xining** | Capital of Qinghai. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 진태경 | 선지자 | enemy commander addressed by Jin | The Prophet | blunt and informal | Jin asks where The Prophet is while confronting the Manticore Lord. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1102
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Cunning and controlling, he avoids costly risks while manipulating allies; beneath his devotion to the Lord of Heaven, he resents being treated as disposable and resents Taekyung’s apparent favor.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven but resents the Lord’s apparent special interest in Jin Taekyung, whom he resolves to kill even if it means defying the Lord’s command; he considers Taekyung and Cheongpung formidable adversaries.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1096
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has also learned concealment from the Slaughter Saint.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, competitive pride, and compassion that leaves him unsettled by killing; he admires Taekyung’s resilience in the way he lives.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint has become his mentor in concealment.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1102
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1102
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1102
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 833
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” who concealed itself for decades as Muninn.
- **Personality:** A calculating, ruthless impostor who exploits followers’ faith and turns to brutal violence when they question or outlive their usefulness.
- **Voice:** Mysterious, genderless, and age-indeterminate, shifting from solemn religious reassurance to cold, contemptuous taunts.
- **Relationships:** The Prophet was revered by his followers and regarded Ahomed as a brother and Disciple; he made a pact with Michael Silbert during the 2020 Battle of Paris.

## Korean source

```text
1103화




일기당천(一騎當千).

불과 몇 년 전의 나는, 저 네 글자에 담긴 뜻과는 매우 거리가 먼 삶을 살고 있었다.

몇 번의 실랑이 끝에 헐값으로 산 중고 장비로 무장하고, 최하급 포션조차 넉넉히 살 수 없었으며, 게이트(Gate)라 불리는 아공간 속 어둡고 습한 동굴과 그곳에서 마주치는 수십여 마리의 소형 몬스터만이 내가 감당할 수 있는 전부였으니까.

그러나 이제는 많은 것이 뒤바뀌었다.

말로는 형용할 수 없는, 그 모든 것이.

퍼걱!

본능처럼 휘두른 녹슨 철검이 측면에서 다가오던 적의 정수리를 파고든다. 두개골이 갈라지고 선홍빛 핏물이 사방으로 비산했다.

투툭.

뺨을 통해 전해지는 끈적하고 뜨거운 감촉.

예전이었다면 그 섬뜩한 감촉에 한 번, 그리고 곧이어 콧속을 파고드는 역한 냄새에 또 한 번 소스라쳤을 것이다.

하지만 난생처음 맡아 보는 끔찍한 피비린내를 참지 못하고 한바탕 속을 게워 냈던 초짜 헌터는, 이제 과거의 기억으로만 남아 있다.

푹!

정면에서 달려드는 적의 목울대에 검신을 쑤셔 박고, 그대로 비틀며 뽑아낸다. 쩍 벌어진 살갗 사이로 핏물이 쏟아졌다.

크륵.

피 가래 끓는 소리와 함께 부르르 떨리는 몸뚱어리.

그러나 이미 오랜 세뇌와 잠력단이 주는 힘에 취한 광신도들에게 있어, 동료의 처참한 죽음은 순교(殉敎)이자 내 빈틈을 노릴 또 다른 기회일 뿐이다.

쉬쉬쉭!

사방에서 핏빛 검기가 빗발친다. 마치 하나의 그물처럼 뒤얽힌 그 촘촘하고도 파괴적인 기운이 내 전신을 뒤덮는다.

아니, 분명 저들의 눈에는 그리 보였을 것이다.

팟.

한 걸음.

단 한 걸음 만에 적들과 나 사이의 공간이 지워진다.

회전하는 신형과 함께 손에 들린 철검이 완벽하면서도 치명적인 궤적을 그려 냈다.

슈확!

일순간, 세상이 멈춘 듯했다.

물러서기는커녕, 되려 자신들의 중심으로 파고든 내 존재를 인식한 적들의 눈동자가 천천히 부풀어 올랐다.

그리고.

콰아아앙!

이미 놈들의 손끝을 떠난 검기의 폭발음과 함께, 수십여 개의 목이 폭죽처럼 솟아올랐다.

서걱, 푸화아악!

붉다.

두 눈으로 보고 있는 시야가. 온 세상이.

하지만 지금 이 순간에도, 내 모든 감각과 신체기관은 쉼 없이 움직이고 있었다.

쉭.

비스듬히 내리그은 검의 궤적에 걸려든 모든 것이 갈라진다.

서서히 높아져만 가는 시체의 산 위를 가로지르는 내 발걸음을 따라, 찐득한 핏물과 그보다도 짙은 비명이 흘러넘쳤다.

퍼걱! 푸푸푹!

막힘없이 베고, 찌르고, 찍었다.

손에 들린 것이 무엇이든 상관없었다.

때로는 도끼, 때로는 검, 혹은 특이한 형태를 지닌 철퇴나 낫과 같은 기병(奇兵)이더라도 그 본질은 결국 살생을 위한 무기였으니까.

콰드드득!

피와 살점이 뒤섞인 폭풍이 휘몰아쳤다.

서녕의 병기고 깊숙한 곳에 처박혀 붉게 녹이 슬어 가던 무기들은 내 손아귀에 잡힌 그 순간 장인의 피땀이 스며든 명기(名器)로 변모했고, 검기에 의해 부러질지언정 기어코 그 본분을 다했다.

주인의 뜻에 따라, 적들의 목숨을 앗아 가는 것으로.

……!

……!!

전후좌우를 둘러싼 적들의, 머리 위 성벽에서 쏟아지는 아군의 고함이 사방을 울린다.

그러나 그들이 무슨 말을 하는지조차 나는 정확히 분간할 수 없었다.

극도로 날 선 감각을 통해 모든 소리를 받아들여야 할 귓가는 먹먹했고, 두 눈으로 보는 세상은 하품이 나올 정도로 느리면서도 선명했다.

지금껏 쓰러트린 적들의 숫자도, 부러진 무기의 개수도 알 수 없었다.

다만, 한 가지는 확신할 수 있었다.

심득(心得).

지금의 나는 또 다른 깨달음을 향한 계단을 오르고 있었다.

주위에서 벌어지는 상황은 물론, 나 자신조차 잊어버리는 무아(無我)의 안개에 휩싸인 채 생과 사가 오가는 전장을 누비고 있었다.

‘더, 조금만 더.’

나는 홀린 듯이 계속해서 마음속으로 뇌까렸다.

어느샌가부터, 내 주위를 둘러싼 모든 것이 꿈결처럼 몽롱하게 느껴진다.

고통인지 쾌감인지 모를 감각이 전류처럼 등골을 타고 흘러내리고 있었다.

이미 과거에도 느껴보았던 감각.

그 어느 때보다 강렬한 무아지경의 감각이 전신을 지배하고 있었다.

‘와라.’

마음속에서만 울려퍼진 그 나직한 속삭임을 들은 듯, 적들이 한 덩어리가 되어 달려든다.

천상천하 만마앙복. 저주와도 같은 그 여덟 글자의 교언(敎言)을 읊고, 고함을 토해 내고, 온 힘을 다해 손에 쥔 병장기를 흩뿌리면서.

동시에 그들 모두가, 한 줌의 고혼(孤魂)이 되었다.

서걱, 서걱, 서걱.

옛 신화 속에 등장하는 선지자가 이러했을까.

거침없이 나아가는 발걸음을 따라 모든 것이 갈라진다.

내 앞에 놓인 것은 결코 바다가 아니었지만, 적들이 뿜어낸 핏물은 파도처럼 휘몰아쳤고 그것은 또 다른 의미의 홍해(紅海)였다.

그리고 좌우로 흘러넘치는 이 붉은 파도 끝에는, 나를 한 단계 더 높은 곳으로 끌어올려 줄 깨달음이 기다리고 있을 터였다.

‘할 수 있다. 분명히.’

점차 흐릿해져만 가는 이성 위로 본능이 덧씌워진다.

뒤에서 휘둘려진 적의 칼날을 보지도 않고 피해 내고, 측면과 정면에서 달려드는 다섯 명의 적들을 일수에 베었다.

하지만 아직도, 그것으로도 부족했다.

나는 불현듯 찾아온 이 꿈결 같은 감각이 영원히 지속되기를 바랐다. 이 꿈은 오직 나만의 것이었고, 어느 때보다 달콤한 단잠이었다.

설령 꿈에서 깨어난다 할지라도, 이 이야기의 끝을 볼 수만 있다면 영혼이라도 팔 수 있었다.

지금 이 순간에도 한 걸음씩 가까워지고 있는 깨달음을 온전히 내 것으로 만든다면, 언제라도 지금과 같은 단잠에 빠질 수 있을 테니까.

그러나 다음 순간, 나는 잠시 망각하고 있던 한 가지 사실을 깨달았다.

꿈을 꾸는 이가 있다면, 그 꿈을 깨우는 자 또한 존재한다는 것을.

쉬이이잉!

주위의 모든 소음을 그저 머나먼 메아리처럼 받아들이던 귓가로 전해지는 한 줄기의 파공성.

그것에 담긴 맹렬함이, 시시각각 다가오는 그 거대한 힘이 나를 강제로 꿈에서 끄집어내어 현실로 내던졌다.

허공 어디에선가 불현듯 터져 나온, 채 끝맺어지지 못한 누군가의 다급한 외침과 함께.

“피하……!”

바로 그 순간.

화악.

내 정신과 몸을 지배하고 있던 무아의 안개가 삽시간에 흩어졌다.

아니, 폭발하듯 터져 나갔다.

그와 동시에 저 멀리서 내달려온 핏빛 섬광이, 그 눈부신 찰나의 번뜩임이 시야를 찐득하게 물들였다.

“……!”

나도 모르게 두 눈이 부릅떠진다. 머릿속에서 울려 퍼진 적색 경종이 속삭이고 있었다.

이미 늦었다고. 이건 피할 수 없다고.

그만큼 나를 향해 쏘아진 섬광은 소름이 끼치도록 빨랐고, 단잠에서 깨어나 현실로 곧장 내동댕이쳐진 내 움직임은 그 속도를 온전히 따라잡을 수 없었다.

그보다 반 박자 앞서 위험을 경고한, 어쩌면 줄곧 내 안위를 예의주시하고 있었던 누군가와는 다르게.

슈확!

느려진 세상 속, 허공에서 떨어져 내리는 한 사람의 신형이  내 망막에 비친다.

어느덧 내 코앞까지 다가온 섬광을 가로막는 새하얀 검신과, 꽃잎처럼 흩날리는 자줏빛의 검강(劍罡)도 함께.

‘청풍(靑風).’

정지되어 있던 사고 속에서 한 사람의 이름이 떠오른 순간.

콰아아아앙!

하늘이 쪼개지는 듯한 굉음과 함께, 거대한 충격파가 공간을 뒤흔들었다.



* * *



쿨럭.

사방을 뒤덮은 희뿌연 먼지구름 속, 메마른 기침을 토해 낸 진태경은 멍하니 눈을 깜빡이며 생각했다.

‘아직, 살아 있는 건가?’

문득 뇌리에 떠오른 의문.

그리고 그에 대한 답은 곧장 되돌아왔다.

바늘처럼 전신을 들쑤시는 크고 작은 통증과 오직 그만이 들을 수 있는 시스템 알림으로.

아니, 정확히는 경고음이라 부르는 것이 옳았다.

삐빅! 삐비빅!

쉴 새 없이 귓가를 파고드는 경고음을 애써 무시하며, 진태경은 힘겹게 몸을 일으켜 세웠다.

투두둑.

몸뚱어리를 타고 흘러내리는 돌가루.

무겁고, 아팠다.

모든 감각이 최고조에 다다라있던 무아지경의 상태에서 돌연 깨어나서일까.

육신은 물을 머금은 솜뭉치처럼 축 늘어져 있었으나, 앞서 줄기차게 울려 퍼진 경고음 세례와는 달리 큰 부상은 없는 듯했다.

물론 그럴 수 있던 것도, 마지막 순간 그를 대신해 섬광을 가로막은 한 사람의 도움 덕분이었지만.

“청 소협.”

지치고 갈라진 목소리가 입술을 비집고 흘러나왔지만, 한 치 앞도 분간할 수 없는 먼지구름 속에서는 누구의 것인지 모를 신음만 곳곳에서 울려 퍼질 뿐이었다.

“……청 소협?”

몇 번을 불렀음에도 되돌아오지 않는 대답에 문득 엄습해 오는 불길함.

크게 심호흡한 진태경은 어느새 너덜너덜해진 옷소매를 흩뿌렸다.

퍼엉!

압축된 공기가 폭발한다. 공력이 실린 바람이 자욱하던 먼지구름을 일부나마 몰아내자, 그 너머에 감추어져 있던 광경이 비로소 실체를 드러냈다.

장정 다섯 사람이 어깨를 나란히 할 정도의 공백을 훤히 드러낸 성벽과 사방에 널브러진 채 고통에 찬 신음을 내뱉고 있는 아군의 모습을.

하지만 지금 이 순간에도, 청풍의 모습은 그 어디에도 보이지 않았다.

‘빌어먹을.’

진태경은 자신도 모르게 이를 악물었다.

그리고 이미 무너진 성벽의 잔해과 먼지구름을 뚫고 돌격해오는 적들을 향해 손을 뻗었다.

정확히는, 그들의 등 뒤에 남아 있는 자신의 애병을 향해.

우우웅.

중단전(中丹田)이 열린다. 나직한 공명음과 함께 지면 깊숙이 박혀 있던 한 자루의 창이 힘차게 솟구쳐 주인의 손아귀로 되돌아갔다.

그 앞길을 가로막는 모든 장애물을 모조리 관통하며.

콰드드득!

솟구치는 피 분수.

한껏 기세를 올리며 돌격하던 수십여 명의 적들이 썩은 통나무처럼 쓰러지고, 그 틈을 타 진형을 갖춘 아군이 온 힘을 다해 찰나의 공백을 메웠다.

차차창!

푸푹!

“크아악!”

“막아라! 단 한 놈도 들여보내선 안 된다!”

“쿨럭, 궁수! 궁수들은 어디 있나!”

삽시간에 번져 가는 극심한 혼란.

그리고 무너진 성벽을 둘러싼 난전(亂戰)이 시작된 그 순간에도, 진태경은 온 힘을 다해 적들을 베어 내며 한 사람의 이름을 외치고 있었다.

“청 소협! 청풍!”

하지만 모든 감각을 끌어올려 보아도 돌아오는 대답은 없었다. 

그저 적과 아군이 토해 내는 비명과 고함만이 사방에서 난무할 뿐, 그 빌어먹게도 천진난만한 목소리는 어디에서도 들을 수 없었다.

심장이 뛰는 소리가 천둥처럼 울려 퍼지고, 매 순간마다 숨이 막혀 올 정도로.

‘……설마.’

아니다. 그럴 리 없다.

청풍은, 그 녀석은 이렇게 쉽게 쓰러질 놈이 아니니까.

마치 동화책에 등장하는 주인공처럼, 어떻게든 살아남아 오래오래 행복하게 살 놈이니까.

그런데 어째서일까. 

도대체 왜, 무슨 이유로 이 알 수 없는 불안감은 더욱더 무겁고 짙어지는 것일까.

“이…… 개자식들아!”

분노에 가득 찬 고함과 함께, 진태경은 적들을 향해 달려나갔다.

그건 지금의 이 모든 사태를 만든 침략자들을 향한 분노인 동시에, 깨달음을 얻기 위한 일념에 사로잡혀 있던 멍청한 자신에 대한 자책이었다.

그리고 적들 사이를 누비며 피바람을 불러일으키는 그 눈부신 창날의 끝은, 느린 발걸음으로 이곳을 향해 다가오는 한 사람에게 다가가고 있었다.

바로 그, 혈주(血主)를 향해.
```

## Final English reading copy

```markdown
# Chapter 1103

One Against a Thousand.

Just a few years ago, I’d been living a life that had nothing to do with those four words.

I’d scraped together some secondhand gear at a bargain price after a few rounds of haggling. I couldn’t even afford a decent supply of the cheapest potions. The most I could handle was a few dozen small monsters in the dark, damp caves inside the subspaces known as Gates.

But a lot had changed since then.

More than I could put into words.

*Thwack!*

The rusty iron sword I swung on instinct sank into the crown of an enemy approaching from the side. His skull split, and bright red blood sprayed in every direction.

*Plop.*

A sticky, hot sensation brushed my cheek.

Once, that chilling touch would have made me flinch. Then the foul stench that crawled into my nose would have made me recoil again.

But that rookie Hunter, who’d thrown up at the horrible stench of blood he’d never smelled before, existed only in my memories now.

*Thrust!*

I drove the blade into the throat of the enemy charging straight at me, twisted it, and yanked it free. Blood poured from the gaping wound.

*Grrk.*

His body trembled as a wet rattle rose from his throat.

But to the fanatics, intoxicated by the strength of the Temporary Strength Pills and years of brainwashing, their comrade’s gruesome death was martyrdom—and just another chance to exploit an opening in my guard.

*Shh-shh-shhk!*

Blood-red Sword Energy rained down from every direction. The dense, destructive energy tangled together like a net, covering my entire body.

Or at least, that was what it must have looked like to them.

*Tap.*

One step.

With that single step, the space between my enemies and me vanished.

As I spun, the iron sword in my hand traced a perfect, deadly arc.

*Whoosh!*

For an instant, the world seemed to stop.

The enemies realized that instead of retreating, I’d plunged straight into their midst. Their eyes slowly widened.

And then—

*BOOM!*

As the Sword Energy they’d already unleashed exploded, dozens of heads shot into the air like fireworks.

*Shhk, fwoosh!*

Red.

The world—and everything in my sight—was red.

Yet even now, all my senses and bodily functions kept working without pause.

*Whoosh.*

Everything caught in the slanted path of my sword split apart.

As I crossed the rising mound of corpses, sticky blood and screams—darker still—spilled around my feet.

*Thwack! Thrust-thrust!*

I cut, stabbed, and smashed without pause.

It didn’t matter what I held in my hands.

An axe, a sword, or some oddly shaped weapon like a mace or a scythe—all of them were, at their core, weapons meant to kill.

*Crack!*

A storm of blood and flesh swept through the air.

The weapons that had been left deep in Xining’s armory, rusting red, became masterworks imbued with a craftsman’s blood and sweat the moment they landed in my hands. They might break against Sword Energy, but they still fulfilled their purpose.

By taking the lives of my enemies, just as their new owner intended.

……!

……!!

The enemies surrounding me on all sides, and the shouts of my allies raining down from the wall above, filled the air.

But I couldn’t even make out what they were saying.

My ears, which should have been taking in every sound with razor-sharp senses, felt muffled. The world before my eyes moved so slowly it was almost boring, yet every detail was crystal clear.

I had no idea how many enemies I’d taken down, or how many weapons I’d broken.

I was certain of only one thing.

Insight.

I was climbing another step toward a new realization.

Wrapped in a fog of No-self, forgetting not only the situation around me but even myself, I moved through a battlefield where life and death hung in the balance.

*More. Just a little more.*

As if bewitched, I kept muttering the words in my heart.

At some point, everything around me had begun to feel hazy, like a dream.

A sensation, impossible to tell whether it was pain or pleasure, ran down my spine like an electric current.

I’d felt it before.

Now the sensation of Trance was more intense than ever, taking over my entire body.

*Come.*

As though they’d heard the quiet whisper that echoed only in my heart, the enemies charged at me as one. They recited those eight words, that curse disguised as a creed—“Heaven above and earth below, all demons bow!”—then roared and lashed out with the weapons in their hands, putting all their strength behind each blow.

And in that same instant, every one of them became a lonely soul.

*Shhk. Shhk. Shhk.*

Was this what the prophet in the old myths had been like?

Everything split apart as I strode forward without hesitation.

There was no sea before me, but the blood the enemies spilled surged like waves. It was another kind of Red Sea.

And at the end of those red waves spilling away on either side, an insight awaited—one that would lift me to a higher level.

*I can do this. I know I can.*

Instinct gradually layered over my fading reason.

Without even looking, I dodged the blade swung at me from behind. With one sweep, I cut down five enemies charging from the side and the front.

But still, it wasn’t enough.

I suddenly wanted this dreamlike sensation to last forever. This dream belonged only to me, and it was the sweetest sleep I’d ever known.

Even if I woke from it, I’d sell my soul just to see this story through to the end.

If I could make the insight that drew closer with every step my own, I could fall into this same sweet sleep whenever I wanted.

But then I remembered something I’d briefly forgotten.

If there was someone dreaming, then there was someone who could wake them.

*Whoooooosh!*

Through ears that had been receiving every sound around me as a distant echo came the sharp whistle of something cutting through the air.

The fury in it, the enormous force drawing nearer by the second, dragged me out of my dream and threw me into reality.

Along with someone’s urgent, unfinished shout, suddenly bursting from somewhere in the open air.

“Dodge—!”

At that very moment—

*Fwoosh.*

The fog of No-self that had taken over my mind and body scattered in an instant.

No—it burst apart.

At the same time, a blood-red flash hurtled toward me from far away, its dazzling glimmer staining my vision with a sticky red.

“……!”

My eyes flew open before I knew it. A red alarm rang in my mind, whispering:

*It’s too late. You can’t dodge this.*

The flash shot toward me with such terrifying speed, and I’d been thrown straight from a sweet dream into reality so abruptly that I couldn’t move fast enough to keep up.

Unlike whoever had warned me of the danger half a beat earlier—someone who might have been watching over me the whole time.

*Whoosh!*

In the slowed-down world, the figure of a person falling through the air appeared on my retinas.

A snow-white blade blocked the flash, which was already almost at my nose. Violet Sword Force scattered around it like flower petals.

*Cheongpung.*

The instant his name surfaced in my frozen thoughts—

*BOOM!*

A tremendous shock wave shook the air with a roar like the sky splitting apart.

* * *

*Cough.*

In the dusty haze that covered everything, Jin Taekyung blinked dazedly and wondered:

*Am I still alive?*

The question surfaced in his mind.

The answer came right away.

Small and large pains pricked through his whole body, accompanied by a System alert only he could hear.

No—warning sirens was the more accurate description.

*Beep! Beep!*

Trying to ignore the sirens that kept drilling into his ears, Jin Taekyung struggled to his feet.

*Rumble.*

Stone dust slid off his body.

Heavy. Painful.

Maybe it was because he’d suddenly woken from a Trance in which every sense had been pushed to its limit.

His body sagged like cotton soaked with water. But despite the barrage of warning sirens, he didn’t seem to have any serious injuries.

Of course, he had someone to thank for that: the person who’d blocked the flash in his place at the last moment.

“Young Hero Cheong.”

His tired, cracked voice slipped past his lips. But in the dust cloud, so thick he couldn’t see a hand in front of his face, all he heard were groans from people he couldn’t identify.

“……Young Hero Cheong?”

When no answer came, even after he’d called several times, a foreboding feeling crept over him.

Jin Taekyung took a deep breath and flung out the sleeve that had already been torn to shreds.

*Boom!*

Compressed air exploded. A gust imbued with internal energy swept away part of the dense dust cloud, and the scene hidden beyond it finally came into view.

A gaping hole in the city wall, wide enough for five grown men to stand shoulder to shoulder, and allies sprawled everywhere, groaning in pain.

But even now, there was no sign of Cheongpung.

*Dammit.*

Jin Taekyung clenched his teeth without realizing it.

Then he stretched out his hand toward the enemies charging through the ruins of the broken wall and the dust cloud.

More precisely, toward his beloved weapon, which lay behind them.

*Vooooom.*

His Middle Dantian opened. With a low hum, a spear buried deep in the ground shot upward and returned to its master’s grasp.

It pierced through every obstacle in its way.

*Crack!*

A fountain of blood surged up.

Dozens of enemies who’d been charging with their spirits high fell like rotten logs. Taking advantage of the opening, the allies formed ranks and fought with all their might to close the gap.

*Clang!*

*Thrust!*

“Gaaagh!”

“Hold them! Don’t let a single one through!”

“Cough—Archers! Where are the archers?”

Chaos spread in an instant.

And even as the melee broke out around the breached wall, Jin Taekyung cut down enemies with all his strength, shouting one person’s name.

“Young Hero Cheong! Cheongpung!”

But no matter how keenly he strained his senses, there was no answer.

Only the screams and shouts of friend and foe alike rang out all around him. That damned innocent voice was nowhere to be heard.

His heart thundered in his chest, and every moment made it harder to breathe.

*……No way.*

No. It couldn’t be.

Cheongpung—he wasn’t the kind of guy who’d go down this easily.

Like the hero in a fairy tale, he’d somehow survive and live happily ever after.

Then why?

Why did this inexplicable unease keep growing heavier and darker?

“You… bastards!”

With a shout full of rage, Jin Taekyung charged toward the enemy.

It was anger at the invaders who’d caused all this—but also blame directed at himself, the idiot who’d been consumed by a single-minded pursuit of enlightenment.

And the dazzling point of his spear, cutting through the enemy and raising a storm of blood, was drawing closer to one person approaching at a leisurely pace.

The Blood Lord.
```
