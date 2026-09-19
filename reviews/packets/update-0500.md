<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0500.txt",
      "sha256": "ab9c1af0463e2b12fc3aaf1b4e85e49ff455ded8bf262483f34f2ca2eec6bbdf",
      "bytes": 13596
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d560e3229b42cf0d5385d18cf73cf51aebbaeacf2e27c8db72099517b1f460ff",
      "bytes": 5499
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "77398870babcadc5a73ba78388d06ef1377f8145ec0f6ed030696ff642196e2b",
      "bytes": 158867
    },
    {
      "path": "characters/Jang Taebo.md",
      "sha256": "87d9a038a3b8c66dafcbd40e0d4383b2c2a8bdc92a505ebca4254372724433b0",
      "bytes": 779
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "0dcb63b70703549c924ae4416b7145a1dfde20af0407b26b03d68b069c2904b2",
      "bytes": 1239
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "0d86027ed6c707f4200364791e7f34f26d03a616287b5fb55360b85977392690",
      "bytes": 954
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "ce7464661bec00fd63e2ef6bda5ebca924a6a79b47c0e78dbc36d637da0e0752",
      "bytes": 649
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "eebb6a55d417a0bf58918cb43c8dd3bd0a4d194812edee7631ef94a7e3eedbb2",
      "bytes": 153941
    }
  ],
  "estimated_tokens": 11322
}
-->

# Durable State Update — Chapter 500

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 500. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 500. Profile updates may replace only one
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
  "chapter": 500,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 500,
    "continuity_sources": [500],
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
    "The Zhuge Clan has sealed the exposed Gate gap with a formation, but whether this is a fundamental or permanent solution remains unresolved; the Gate's residual mana previously mutated local life.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, were captured in the Gate's entrance waterways; the remaining population is unknown, and the fish kill one another.",
    "Taekyung suspects Dark Heaven's regeneration, teleportation, and Moving Formation are manifestations of Magic connected to the Gate, and he told Jeok that he came from another world whose evil force is linked to Dark Heaven.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people; the severely injured Dongting Fisherman may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense; Wipeng and the Jin Dragon Squad have joined Jin Wikyung, and Jin Wikyung has established Ironcraft Hall and recruited Jang Taebo as its master.",
    "Jeok's innate qi is damaged and steadily diminishing despite the Thousand-Year Snow Ginseng and the Divine Physician's treatment; Taekyung remains uncertain whether Jeok recovered without lasting aftereffects.",
    "Mungyeong is the Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; before becoming the Slaughter Saint, he was called Killing Ghost, and he saved countless people as the Divine Physician.",
    "Mungyeong recognizes Taekyung's Heavenly Martial Physique as innate and distinct from Cheongpung's more refined physique; after seven days and nights of poisoned tests, he intends to teach Taekyung secret martial arts without a formal Master-Disciple relationship.",
    "Taekyung completed Mungyeong's tests, gained EXP, points, Poison Resistance, sharper Qi Sense, and a clue to enlightenment, while retaining the Water God Dragon's dismantled materials and Origin Essence after permanently losing 5 Strength and 5 Agility from Sinews and Meridians damage.",
    "The Mount Heng Sword Sect has completed its reconstruction and is growing under Lee Seowol, while Cheol Mubaek has ended his seclusion and is helping manage the sect's affairs.",
    "Jin Mukyung has remained secluded in the training hall for more than a year after losing to Cheongpung, subsisting on fasting pills while refusing to emerge until he achieves a great accomplishment."
  ],
  "continuity_sources": [
    499,
    498
  ],
  "open_questions": [
    "Will Zhuge Feng's formation permanently seal the Gate gap, and what lies beyond it if the Gate is reopened?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "Has Jeok fully recovered from the Formless Ultimate Poison, and will Taekyung use the Water God Dragon's Origin Essence to aid him?"
  ],
  "safe_through": 499,
  "temporary_decisions": [
    "Render 산공독 as Energy-Dispersing Poison, 강력한 산공독 as Potent Energy-Dispersing Poison, 칠보추혼산 as Seven-Step Soul-Chasing Powder, 강력한 칠보추혼산 as Potent Seven-Step Soul-Chasing Powder, 심각한 복통 as Severe Stomachache, 고기 방패 as Meat Shield, 독 장아찌 as Poisoned Pickle, and 독의 as Poison Physician; retain secret martial arts, Master-Disciple relationship, Killing Ghost, and Fake Murim Martial Artist, and preserve 악 as Agh in the Quest interface; render 실명산 as Blindness Powder, 살천문 as Salcheonmun, and 스승의 날 as Teacher’s Day.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 혈어 as Blood Fish, and 변이된 송사리 as Mutated Minnow; render 강력한 마비산 as Potent Paralysis Powder, 강력한 미혼산 as Potent Soul-Bewitching Powder, 전신 마비 as Full-Body Paralysis, 독성 흡수 as Poison Absorption, and 해독 as Detoxification.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter; render 해시 as hour of the Pig, 한 식경 as half an hour, 타구봉 as Dog-Beating Staff, 창룡 as Azure Dragon, and 무량수불 as Infinite Life Buddha; preserve geun as the traditional weight unit with a footnote.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, and 천기 as heavenly patterns.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 강강수월래 as Ganggangsullae, 생사부 as Book of Life and Death, 기막 as qi curtain, 무극태을검 as Martial Extremity Grand Unity Sword, 이룡 as Two Dragons, 원정 as Origin Essence, 내단 as inner core, 영험한 기운 as sacred energy, 대호 as great tiger, 취팔선권 as Drunken Eight Immortals Fist, 귀면 as Ghost Face, 요단강 as Jordan River, and 진룡 as Jin Dragon."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 위팽     | **Wipeng**         |
| 삼성     | **Three Saints**    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 진룡대    | **Jin Dragon Squad**             |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 제갈세가   | **Zhuge Clan**                   |
| 무인     | **martial artist**                               | Default term                                          |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 큰형     | **eldest brother**                           |
| 명성               | **Fame**                       |
| 체력               | **Stamina**                    |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 대격변     | **Great Cataclysm**   |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 장태보 | **Jang Taebo** | Former Guild Leader of the Ironcraft Guild; now lives near Jeongyang and is sought as a Master Artisan. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 대태원진가 | **great Jin Family of Taiyuan** | Formal exalted reference to the Jin Family of Taiyuan. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 명장 | **Master Artisan** | Master craftsman capable of handling Ten-Thousand-Year Cold Iron |
| 철기방 | **Ironcraft Guild** | Hubei guild composed mainly of skilled craftsmen and closely associated with the Nine Sects and One Gang. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 기관진식 | **mechanisms and formations** | Fifth preliminary assessment category. |
| 제갈무후 | **Zhuge Wuhou** | Honorific title for Zhuge Liang in the Three Visits allusion. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 운철 | **meteorite iron** | Material whose strength is used as a comparison for the black-wood fishing rod. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 진룡 | **Jin Dragon** | The two characters embroidered on the Jin Dragon Squad's uniforms. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진위경 | 막내 | older brother to younger brother | my youngest | intimate and informal | Jin Wikyung uses 막내야 affectionately for Jin Taekyung. |
| 제갈풍 | 진위경 | Zhuge Clan Family Head to Jin Family Lesser Family Head | Lesser Family Head | formal and conciliatory | Uses 소가주 while trying to secure Jin Wikyung's support during the settlement. |
| 진위경 | 제갈풍 | Jin Family Lesser Family Head to Zhuge Clan Family Head | Sir Zhuge | formal with deliberate comic deference | Uses 제갈 대협 while theatrically scolding Taekyung to force Zhuge Feng to concede. |
| 진위경 | 장태보 | Lesser_Family_Head_to_elder_smith | Old Master Jang | respectful and formal | Wikyung thanks Jang for coming. |
| 장태보 | 진위경 | elder_smith_to_Lesser_Family_Head | Lesser Family Head | respectful and deferential | Jang speaks with formal respect to Wikyung. |

## Listed compact profiles

### Jang Taebo.md

# Jang Taebo (장태보)

- **Safe through:** Chapter 499
- **Aliases:** None
- **Role:** Jang Taebo is the former Guild Leader of the Ironcraft Guild and one of the world’s renowned smiths, now the Jin Family of Taiyuan’s Master of Ironcraft Hall..
- **Personality:** Blunt, cantankerous, solitary, and proud; values an untroubled retirement and protects his anonymity, while quietly caring for the neighboring boy Hanga.
- **Voice:** Curt, gruff, and dryly teasing; rejects requests with flat finality.
- **Relationships:** His disciple is the current Guild Leader of the Ironcraft Guild; neighboring boy Hanga is his only conversational partner, and Jang Taebo gives him candy while pretending annoyance.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 499
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 499
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and Commander of the Jin Dragon Squad; one of the Jin Family’s three Peak masters
- **Personality:** Loyal, observant, teasing, capable, and resigned to Jin Wikyung’s impulsive behavior. Respects the dead and urges others to live on their behalf.
- **Voice:** Weary and knowing, with dry humor when addressing Jin Wikyung or Jin Taekyung. Uses Sound Transmission when appropriate.
- **Relationships:** Trusted guard and retainer of Jin Wikyung; a reliable senior ally of Jin Taekyung. He has fought beside the Jin Family in major battles, including the conflict with Mount Heng, and remains alert to threats connected with Dark Heaven. The Human Butcher has claimed him as a personal target in a planned attack.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 496
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical, disarmingly casual, eccentric, and inventive; he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃500화



동이 트기도 전인 깊은 새벽, 죽을상을 하고 따라나선 장태보는 수신룡의 부산물을 보자마자 돌변했다.

“오오, 오오오……!”

태세전환 보소.

오줌 마려운 유치원생처럼 몸을 바르르 떨던 장태보가 산더미처럼 쌓인 뼈와 비늘 사이로 몸을 던졌다.

“오오, 이 강도! 이 빛깔!”

몽롱하게 풀어진 눈동자와 떨리는 목소리. 비늘을 더듬고 뼈를 어루만지는 손길에 숨길 수 없는 흥분과 기쁨이 묻어 나왔다.

“이대로 파묻혀 죽어도 좋아! 아니, 죽을래!”

“노야를 구출해라! 사체가 무너지려고 한다!”

“조, 존명!”

지금껏 본 적 없는 거대한 생물체의 부산물을 넋 놓고 바라보던 진룡대원들이 달려가 장태보를 끄집어냈다.

그제야 정신을 차린 늙은 명장(名匠)은 촉촉해진 눈가로 나를 바라보았다.

“그 말이 전부 사실이었다니.”

“미친 얘기 같지만 전부 사실이에요.”

“저 하늘에서 떨어진 운철(隕鐵)도 다뤄 보고, 만년한철(萬年寒鐵)도 원 없이 주물러 봤다고 생각했건만…….”

장태보가 울컥한 표정으로 눈가를 문지른다. 감정을 다스리며 코를 훌쩍거리던 그가 내 어깨를 덥석 움켜쥐었다.

“고맙다. 내 이제 죽어도 여한이 없구나.”

나는 따뜻한 눈빛으로 장태보를 응시했다.

“그런 말 마시고 몸 건강히 장수하십시오. 건강에 좋은 것도 푹 고아 드시고요.”

“네 녀석…….”

“앞으로 남아 있는 체력과 생명을 대장간에 갈아 넣으셔야죠. 어딜 저승으로 튀시려고.”

“네 녀석……!”

같은 말. 다른 느낌.

어렵게 확보한 고급 노비인 만큼 확실하게 부려먹어야 한다. 가끔은 떡고물도 주고, 채찍도 휘두르고.

물론 채찍을 쥔 사람은 내가 아니라 다른 누군가다.

“허어, 다시 봐도 놀랍구나. 물량도 어마어마해.”

“채찍 주인 어서 오고.”

“응? 뭐라 하였느냐, 막내야?”

“아닙니다, 큰형님.”

고개를 갸웃거린 진위경이 이내 껄껄 웃으며 장태보의 등을 두드렸다.

“어떻소, 장 당주. 실로 엄청난 광경이지 않소!”

“장…… 당주?”

“허허, 당연한 것 아니겠소. 본가의 철기당주가 되셨으니 장 당주지. 자, 이제 고견을 들려주시구려.”

잠시 잊고 있던 현실을 슬슬 깨닫게 된 장태보가 어두운 얼굴로 대답했다.

“후우, 두말할 필요 없지요. 천하에서 내로라하는 장인과 재료가 모인 철기방에서도 이러한 광경은 보지 못했습니다.”

“해서, 할 수 있겠소?”

“직접 해 보기 전까지는 무엇도 장담할 수 없지요. 다만…….”

산더미처럼 쌓인 부산물을 신중한 눈빛으로 살핀 장태보가 말을 이었다.

“뼈의 강도가 운철 이상으로 대단하나 만년한철보다는 못하니, 충분히 다루어 봄 직합니다.”

“가죽과 비늘은 어떻소?”

“갑옷이라면 소싯적에 질리도록 만들어 보았습니다. 비록 재료가 이무기의 것은 아니었지만…… 해 보지요.”

“오오.”

“이 정도 물량이라면 태원진가, 아니 본가의 무인들을 전부 무장시키고도 남을 터. 곧 성과를 보일 터이니 처음 몇 번의 실패 정도는 용납해 주시리라 믿습니다.”

“이를 말이겠소.”

장인으로서의 장태보는 무림인으로 치자면 삼성(三星)과 같거나 그 이상의 위치에 있는 인물이다.

담담하지만 근거 있는 자신감을 내비치는 고급 노비의 말에 진위경의 얼굴이 환하게 밝아졌다.

“철기방의 방주는 당대에서 제일가는 명장만이 될 수 있다고 들었소. 내 장 당주만 믿을 테니 필요한 것이 있다면 무엇이든 말씀하시구려.”

“그럼 믿을 만한 장인들을 붙여 주십시오, 소가주님.”

“장인들이라.”

“본가에도 장인들이 있다는 건 알고 있습니다. 제가 그들을 가르친다면 향후 본가를 받치는 대들보는 아니어도, 제법 튼튼한 기둥 정도는 되겠지요. 하지만…….”

“적지 않은 시간이 걸리겠지. 맞소?”

“그렇습니다. 저도 눈과 귀가 있어 근래 천하에서 일어나는 일들은 익히 들어 알고 있습니다. 근근이 연락을 주고받는 장인들도 병장기 관련 주문이 급증했다고 알려 주더군요.”

전쟁은 이미 시작되었다.

천하 무림 곳곳에 산재한 중소 문파부터 구파일방까지. 모두가 성큼 다가온 전란에 대비한 병장기를 원하고 대장간의 불꽃은 전쟁이 끝날 때까지 꺼지지 않을 것이다.

작금의 천하에서, 맹렬히 타오르기 시작한 것은 전화(戰火)의 불꽃만이 아니었다.

“시간이 촉박합니다, 소가주님.”

말없이 하늘을 바라보던 진위경이 문득 입을 열었다.

“장 당주, 그대는 이 일을 몇 년이나 해 왔소?”

“소가주님의 검보다 키가 작을 무렵부터 시작했지요. 제 일생을 바쳤습니다.”

“그 오랜 세월을 한 분야에 몰두했으니, 함께 일했던 벗들도 많았겠구려.”

“이를 말이겠습니까. 하나하나가 각 분야에서 내로라하는 장인들입니다.”

“지금 그대의 머릿속에 떠오른 이들 모두에게 전서구를 띄우시오. 억만금의 재물이 들어가도 상관없소.”

“사람마다 재물보다 귀하고 소중하게 여기는 것이 있지요. 이 늙은이 같은 장인에게는 이무기의 몸뚱어리가 억만금보다 값진 것입니다.”

한 걸음 뒤로 물러난 장태보가 진위경을 향해 공손히 포권을 취했다.

“대태원진가 철기당주 장태보. 소가주님의 명을 받드옵니다.”

어느새 어둠이 물러가고 새로운 날의 해가 떠오른다. 동쪽으로부터 번져 오는 빛은 대장간의 불길을 닮았고, 신속하게 수신룡의 사체를 옮기는 진룡대 무인들의 발걸음은 망치질과 같았다.



* * *



진룡대의 무인 오십 명이 위팽과 장태보의 철두철미한 지휘하에 수신룡의 사체를 실어 나르는 동안, 원래 있어야 할 곳으로 돌아온 나와 진위경은 잔뜩 흥분한 제갈풍과 마주했다.

“해냈어! 내가 해냈단 말이오!”

어린아이처럼 펄쩍 뛰는 모습에서 일가의 가주가 보여야 할 체통이라고는 찾아볼 수가 없다.

하지만 잠시 후, 결과물을 확인한 나로서는 고개를 끄덕이지 않을 수 없었다.

‘마력(魔力)을 완전히 틀어막았어.’

거대한 균열, 아니 게이트에서는 처음과 달리 미세한 마력조차 흘러나오지 않았다.

실험을 위해 놔둔 것처럼 보이는 개와 돼지, 물고기 따위도 몇 번 관심을 보이더니 제 할 일에 몰두했다.

“기어코 해내셨군요, 제갈 대협.”

진위경의 말에, 피곤에 찌든 제갈풍의 얼굴 위로 활짝 웃음꽃이 피어올랐다.

“나니까 해낸 거요. 선조이신 제갈무후(諸葛武侯)께서도 못 하셨을 일이지. 생각해 보면 그분께서도 기관진식에 소양이 있으셨지만 결국 위나라에 개처발렸…….”

“가, 가주님!”

“아, 왜. 사실이지 않나! 백성을 생각하는 승상이자 진정한 책사였다면 무능한 황제의 면상에 출사표가 아니라 사표를 내던지고 황위를 찬탈했어야…….”

“가주, 진정 미친 거요!”

“아니, 백부님. 제가 틀린 말 했습니까?”

제갈세가도 개판이구만.

선조의 명성에 똥을 퍼 바른 현 가주는 친인척들을 뿌리치고 의기양양하게 말을 이었다.

“어떤가, 마봉진(魔封陣)을 직접 본 소감이?”

“마봉진?”

제갈풍이 흐뭇하게 고개를 끄덕였다.

“내 직접 이름을 붙였지. 마귀의 힘을 봉인하는 진법. 어울리지 않나?”

마봉진이라. 저 힘의 근원을 생각해 보면 이것만큼 어울리는 명칭이 없다.

사실 진법의 명칭이야 어찌 되었건, 효과만 확실하다면 무슨 상관이겠나.

신중하게 마봉진을 살피는 내게, 진위경이 작게 속삭였다.

“어떤 것 같으냐?”

“뭘요?”

“……?”

“그냥 보는 건데요. 제가 어떻게 압니까?”

무림의 진법은 현대의 마법진이나 마찬가지다.

그나마 헌터로 살면서 자주 접한 마법에도 문외한인 내가, 진법을 한눈에 보고 판단할 수 있을 리가 있나.

그나마 깜냥이 있어 진법을 타고 흐르는 기의 흐름을 느낄 수 있을 뿐이다.

‘대자연에 있는 기운을 끌어와 마력을 막고 있는 것 같은데…… 작동 원리는 마법진이랑 비슷하군.’

하지만 지금까지 무림에서 보고 들은 진법은 현대의 마법진에 비하면 그 종류나 위력이 훨씬 떨어진다.

그럴 수밖에 없는 이유에는 무(武), 자체를 숭상하는 무림인들의 기조가 크게 한몫했을 테고.

‘이 정도면 생각했던 것 이상으로 빠르게, 그리고 잘해 줬어.’

진법을 타고 흐르는 대자연의 기운은 게이트에서 새어 나오는 마력을 완전히 틀어막기에 충분했고, 현재로서는 이게 최선의 방책이라고 할 수 있다.

마봉진을 꼼꼼히 살핀 나는 제갈풍을 향해 고개를 돌렸다.

“이 마봉진의 효력이 얼마나 더 지속될까요?”

“자네는 장강의 강물이 마른 적이 있다고 생각하나?”

“아하.”

“마봉진은 주위의 기운을 계속해서 끌어모아 가동될 걸세. 내가 정립한 이론대로라면 말이지.”

“그럼 제갈 대협의 이론이 어긋날 경우는요?”

“내가? 차라리 제갈무후께서 반푼이였다고 하게.”

차창!

“네 이놈, 제갈풍!”

“안 됩니다, 작은할아버지! 검을 내려놓으십시오!”

“누가 가주님의 입을 틀어막아라!”

거 분위기 한 번 살벌하다.

나는 골육상잔의 피바람이 불기 직전, 달려드는 가솔들을 상대로 금나수를 펼치는 제갈풍을 향해 서둘러 말을 이었다.

“그럼 이걸 앞으로도 계속 설치할 수 있습니까?”

“어?”

“응?”

“뭐요?”

나는 우뚝 굳어 버린 제갈세가의 사람들을 위해 또렷한 발음으로 재차 입을 열었다.

“앞으로도 계속. 그러니까 수십, 수백 번 말입니다.”

“……!”

“……!”

순간 주위의 공기가 싸늘하게 얼어붙었다.

웬 노인에게 멱살을 붙잡혀 있던 제갈풍이 옷매무새를 가다듬었다. 이어 착 가라앉은 눈빛과 목소리가 나를 향해 쏟아졌다.

“문득 궁금해지는군. 신룡(神龍)의 의중이.”

나는 씁쓸하게 입맛을 다셨다.

“뻔한 이야기죠. 제갈 대협께서도 이미 알고 계시잖습니까.”

“알지. 한 번 벌어진 일은 열 번, 백 번도 가능하다는 것도.”

“그럼 저와 같은 생각이시겠네요.”

“자네처럼 확신하지는 못했지. 그저 향후 일어날 수 있는 모든 상황을 염두에 둔 것일 뿐이야.”

제갈풍의 눈동자가 알 수 없는 빛으로 번뜩였다.

“어찌하여 이런 일이 계속 생기리라 장담하나? 그리도 확신에 차서 말할 수 있는 근거가 뭔가?”

근거야 많다. 말해 줄 수가 없어서 그렇지.

제갈풍이 탄생하던 날, 제갈세가가 기쁨에 들썩였겠지만 내가 태어나던 날에는 전 인류가 들썩였다.

마왕 아스모데우스가 쓰러지고, 길었던 대격변이 막을 내렸으니까.

이건 어떤 말로도 설명할 수 없는 차이다.

그 뒤로 내가 먹은 나이만큼의 시간이 흘렀지만 현대에는 아직 게이트가 남아 있고, 새롭게 생성되기를 반복했다.

제아무리 견고한 둑이라도 한 번 금이 가기 시작하면 걷잡을 수 없는 법.

작금의 무림이 바로 그렇다.

‘이걸 속 시원하게 털어놓을 수도 없고.’

결국 내가 할 수 있는 대답은 처음부터 정해져 있는 것이나 다름없었다.

“수신룡이 전해 준 기억 속에서 직접 보고 느꼈습니다. 이건 암천이 처음부터 의도하고, 계획하고, 실행에 옮긴 짓이라는 것을. 그리고 앞으로도 계속될 겁니다.”

“생각보다 거짓말에 능숙하군.”

“생각보다 의심이 많으시네요.”

“믿지 못하겠네. 아니, 믿기 싫다는 게 솔직한 마음이겠지.”

“제갈무후도 그랬을 겁니다. 그래도 마지막까지 멍청한 황제를 보필하지 않았습니까. 좆 같아도 받아들여야죠.”

“좆 같아도 받아들여야 한다…….”

피식 실소를 흘린 제갈풍이 한 사람을 향해 고개를 돌렸다.

“소가주의 생각은 어떠시오?”

진위경이 담담한 목소리로 대답했다.

“저 역시 아우의 생각과 같습니다.”

“다른 이들의 생각은 어떨지, 참으로 궁금해지는구려.”

“그렇다면 다 함께 묻고, 들으면 되지 않겠습니까.”

“그게 무슨…….”

진위경을 응시하던 제갈풍이 문득 중얼거렸다.

“하남.”

“예.”

진위경이 저 어딘가를 바라보며 말을 이었다.

“신(新) 무림맹입니다.”
```

## Final English reading copy

```markdown
# Chapter 500

In the dead of night, before dawn had even begun to break, Jang Taebo had followed us along with a face that looked ready for the grave.

But the moment he saw the Water God Dragon’s remains, he changed completely.

“Ohhh… Ohhhhh…!”

Talk about a complete change of attitude.

Jang Taebo, who had been trembling like a kindergartener who needed to pee, threw himself between the mountains of bones and scales.

“Oh, the strength! The color!”

His eyes were unfocused with rapture, and his trembling voice betrayed his excitement. His hands ran over the scales and gently caressed the bones, unable to hide his joy.

“I’d be happy to be buried here and die! No, I want to die here!”

“Rescue Old Master! The remains are about to collapse!”

“Y-yes, sir!”

The Jin Dragon Squad martial artists had been staring blankly at the remains of a gigantic creature unlike anything they had ever seen. Now they rushed forward and dragged Jang Taebo out.

Only then did the old Master Artisan come to his senses. He looked at me with moist eyes.

“So everything you told me was true.”

“It sounds insane, but every word of it was true.”

“I thought I had handled meteorite iron that fell from the sky and worked Ten-Thousand-Year Cold Iron to my heart’s content…”

Jang Taebo wiped at the corners of his eyes with a deeply moved expression. After sniffing and composing himself, he suddenly grabbed my shoulder.

“Thank you. I can die without regrets now.”

I gazed at Jang Taebo warmly.

“Don’t say things like that. Live a long, healthy life instead. And have something nourishing slow-simmered for yourself, too.”

“You little…”

“You still have plenty of Stamina and life left to grind into the forge. Where are you trying to run off to—the afterlife?”

“You little…!”

The same words. A completely different feeling.

A high-quality slave this difficult to acquire had to be put to proper use. Every now and then, I would give him a little reward and crack the whip.

Of course, I wasn’t the one holding the whip.

“Good heavens. It’s astonishing even after seeing it again. There’s an incredible amount of material here.”

“Welcome, owner of the whip.”

“Hm? What did you say, my youngest?”

“Nothing, eldest brother.”

Jin Wikyung tilted his head, then laughed heartily and patted Jang Taebo on the back.

“How do you find it, Hall Master Jang? It’s a truly spectacular sight, isn’t it?”

“Hall Master… Jang?”

“Heh heh. Of course. You are now the Hall Master of our family’s Ironcraft Hall, so that makes you Hall Master Jang. Come, let us hear your expert opinion.”

Jang Taebo slowly began to understand the reality he had momentarily forgotten. He answered with a dark expression.

“Whew. There’s no need to say anything more. Even at the Ironcraft Guild, where the finest artisans and materials under Heaven were gathered, I never saw anything like this.”

“So, can you do it?”

“I can’t guarantee anything until I try it myself. However…”

Jang Taebo carefully examined the remains piled up like a mountain before continuing.

“The bones are far stronger than meteorite iron, though not quite as strong as Ten-Thousand-Year Cold Iron. They should be workable.”

“What about the hide and scales?”

“As for armor, I made enough of it in my younger days to grow sick of the work. The materials weren’t from an imugi, of course…but I’ll give it a try.”

“Ohh.”

“With this much material, there will be enough to arm every martial artist in the Jin Family of Taiyuan—or rather, in our family—and still have some left over. I should be able to show results soon, so I trust you’ll forgive the first few failures.”

“Of course.”

As a craftsman, Jang Taebo stood at a position equal to or higher than the Three Saints among martial artists.

Jin Wikyung’s face brightened at the measured but well-founded confidence of the high-quality slave.

“I’ve heard that only the finest Master Artisan of the age can become the Guild Leader of the Ironcraft Guild. I’ll be counting on you, Hall Master Jang, so tell me if you need anything.”

“Then please assign some trustworthy artisans to me, Lesser Family Head.”

“Artisans?”

“I know our family has artisans of its own. If I teach them, they may not become the beams supporting the family, but they should at least grow into fairly sturdy pillars. However…”

“It will take no small amount of time. Am I right?”

“That is correct. I have eyes and ears, so I’ve heard plenty about what has been happening throughout the world lately. The artisans I still exchange occasional letters with have told me that orders for weapons and armor have increased sharply.”

The war had already begun.

From the small and mid-sized sects scattered throughout Murim to the Nine Sects and One Gang, everyone wanted weapons and armor to prepare for the war that had drawn so close. The fires of the forges would not go out until the war ended.

In the current state of Murim, it was not only the flames of war that had begun to blaze fiercely.

“Time is short, Lesser Family Head.”

Jin Wikyung silently gazed up at the sky before suddenly speaking.

“Hall Master Jang, how many years have you been doing this work?”

“I began when I was shorter than your sword, Lesser Family Head. I devoted my entire life to it.”

“You spent all those years immersed in one field, so you must have made many friends while working alongside them.”

“Of course. Every one of them is a renowned artisan in their respective field.”

“Send messenger pigeons to every one of them who has just come to mind. I don’t care if it costs a fortune.”

“Everyone has something they value more dearly than wealth. For a craftsman like this old man, the body of an imugi is worth more than a fortune.”

Jang Taebo took one step back and performed a respectful martial salute toward Jin Wikyung.

“Jang Taebo, Master of Ironcraft Hall of the great Jin Family of Taiyuan, obeys the Lesser Family Head’s command.”

Before anyone realized it, the darkness had receded and the sun of a new day had risen.

The light spreading from the east resembled the flames of a forge, while the footsteps of the Jin Dragon Squad martial artists swiftly carrying the Water God Dragon’s remains sounded like the ringing of hammers.

* * *

While fifty Jin Dragon Squad martial artists transported the Water God Dragon’s remains under the meticulous direction of Wipeng and Jang Taebo, Jin Wikyung and I returned to where we were supposed to be and encountered Zhuge Feng, who was brimming with excitement.

“I did it! I’m telling you, I did it!”

He jumped around like a child. There was no sign of the dignity one would expect from the Family Head of a great clan.

However, after checking the result for myself, I had no choice but to nod.

*He completely blocked the mana.*

Unlike before, not even the slightest trace of mana flowed from the enormous rift—or rather, the Gate.

The dogs, pigs, fish, and other creatures that had been left behind as though for an experiment showed some interest in it a few times, then returned to whatever they had been doing.

“You actually managed to do it, Sir Zhuge.”

At Jin Wikyung’s words, a brilliant smile bloomed across Zhuge Feng’s exhausted face.

“I pulled it off because I’m me. Even my ancestor Zhuge Wuhou couldn’t have accomplished something like this. Come to think of it, he had some knowledge of mechanisms and formations, too, but in the end, Wei fucking trounced him…”

“F-Family Head!”

“Ah, why? Isn’t it true? If he really was a chancellor who cared about the people and a true strategist, he should have thrown a resignation letter in that incompetent emperor’s face instead of a campaign memorial and seized the throne…”

“Family Head, you really are insane!”

“Uncle, did I say anything wrong?”

The Zhuge Clan was a real mess.

The current Family Head, having smeared shit all over his ancestor’s reputation, shook off his relatives and continued speaking proudly.

“Well? What do you think after seeing the Demon-Sealing Formation for yourself?”

“The Demon-Sealing Formation?”

Zhuge Feng nodded with satisfaction.

“I named it myself. A formation that seals the power of demons. Doesn’t it suit the purpose?”

The Demon-Sealing Formation. Considering the source of that power, there couldn’t have been a more fitting name.

Of course, what the formation was called didn’t matter as long as it worked.

As I carefully examined the Demon-Sealing Formation, Jin Wikyung whispered to me.

“What do you think?”

“About what?”

“……”

“I’m just looking at it. How would I know?”

Murim formations were essentially the same as modern magic circles.

Even though I had often encountered Magic while living as a Hunter, I was hardly an expert. There was no way I could look at a formation once and judge it.

At most, I had enough aptitude to sense the flow of qi moving through it.

*It seems to be drawing in the qi of the natural world to block the mana…but its operating principle is similar to a magic circle.*

However, compared to modern magic circles, the formations I had seen and heard about in Murim were far more limited in variety and power.

The Murim’s reverence for martial arts itself had probably played a major role in that.

*They did this faster and better than I expected.*

The qi of the natural world flowing through the formation was sufficient to completely block the mana leaking from the Gate. For now, this was the best possible solution.

After examining the Demon-Sealing Formation thoroughly, I turned toward Zhuge Feng.

“How long will this formation remain effective?”

“Do you think the waters of the Yangtze have ever dried up?”

“Ah.”

“The Demon-Sealing Formation will continue drawing in the qi around it and remain active. At least, that’s what my theory says.”

“And what if Sir Zhuge’s theory is wrong?”

“My theory? You might as well say Zhuge Wuhou was a halfwit.”

Clang!

“You bastard, Zhuge Feng!”

“Great-Uncle, no! Put down your sword!”

“Someone shut the Family Head’s mouth!”

The atmosphere had suddenly turned murderous.

Before a bloody storm of familial slaughter could break out, I hurriedly continued speaking to Zhuge Feng as he used a grappling technique against the relatives rushing at him.

“Then can you keep installing this in the future?”

“Huh?”

“What?”

“What do you mean?”

For the sake of the Zhuge Clan members who had frozen in place, I repeated myself with clear enunciation.

“Continuously. I mean dozens or even hundreds of times.”

“……!”

“……!”

The air around us instantly turned cold.

Zhuge Feng, who had been grabbed by the collar by an old man, straightened his clothes. Then his eyes and voice sank as they turned toward me.

“I suddenly find myself curious about the Divine Dragon’s intentions.”

I gave a bitter smack of my lips.

“It’s obvious, isn’t it? You already know, Sir Zhuge.”

“I do. I know that something which has happened once can happen ten times or a hundred times.”

“Then you must think the same way I do.”

“I wasn’t as certain as you. I was merely taking every situation that might arise in the future into account.”

An unreadable light flashed in Zhuge Feng’s eyes.

“Why are you so certain that things like this will continue happening? What grounds do you have for speaking with such confidence?”

I had plenty of grounds. I simply couldn’t tell him about them.

The Zhuge Clan might have been abuzz with joy on the day Zhuge Feng was born, but on the day I was born, all of humanity was abuzz.

The Demon King Asmodeus had fallen, and the long Great Cataclysm had finally come to an end.

It was a difference that could not be explained in words.

After that, as many years passed as I had lived, but Gates still remained in the modern world and continued appearing again and again.

No matter how sturdy a dam was, once it began to crack, the damage would soon become impossible to control.

The current Murim was exactly the same.

*I can’t exactly tell them all of this.*

In the end, the answer I could give had been decided from the beginning.

“I saw and felt it directly in the memories the Water God Dragon passed on to me. This was something Dark Heaven intended from the very beginning, planned, and carried out. And it will continue.”

“You’re more skilled at lying than I expected.”

“You’re more suspicious than I expected.”

“I can’t believe you. No—the honest truth is that I don’t want to believe you.”

“Zhuge Wuhou must have felt the same way. And yet he still served that stupid emperor until the very end. Even if it fucking sucks, you have to accept it.”

“Even if it fucking sucks, you have to accept it…”

Zhuge Feng let out a quiet laugh and turned toward one person.

“What do you think, Lesser Family Head?”

Jin Wikyung answered in a calm voice.

“I think the same as my younger brother.”

“I wonder what the others think.”

“Then why don’t we ask them and hear for ourselves?”

“What does that mean…?”

Zhuge Feng stared at Jin Wikyung, then suddenly muttered,

“Henan.”

“Yes.”

Jin Wikyung looked toward somewhere in the distance and continued.

“The New Murim Alliance.”
```
