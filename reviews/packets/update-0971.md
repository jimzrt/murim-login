<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0971.txt",
      "sha256": "f1f65047f4617cb5e45f12a4ba04901118ac1fd20196a89b4894604d59119257",
      "bytes": 12867
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "55496ef974b35a737c1ca1adc5e07a75ac9cbd402d7b6934a58f46a1837b7523",
      "bytes": 1451
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "65892110351fce017f8020b13720d8c5e71418799da1db239060ea308ecc01e4",
      "bytes": 235501
    },
    {
      "path": "characters/Cheolyeong.md",
      "sha256": "e8df2636d0f0f70e50aeec31b18b30a87935e6d0d75a79ad342abdef5df48b59",
      "bytes": 342
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "4579cc8ad496f009f65ab3f8890fe209d3c107b5e3dd353bdd7d8c4f56d29f89",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "48d1fe857ecb4465adfc6376e2f2220be30ed5f5f3beede0465744af6ab1f79c",
      "bytes": 838
    },
    {
      "path": "characters/Jamukha.md",
      "sha256": "34c7b653a378d907dd92380fa6ed939adc79481f8124591e35269d7f386bcf02",
      "bytes": 574
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "64485e513239a4147e02be6b1ef2b837db33f8495922560e21d885b435fce02e",
      "bytes": 1204
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "b02dc98ad99307853a75dd488add89dcc908c3e99b2f3d581c32ce6e5aa74187",
      "bytes": 1405
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "de01086d504d4d071f082cd69607a7feddfb3a2082c7af65a1fe94dbd325677f",
      "bytes": 1481
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "92670350470ffee6018170e8215f201316dd184bd96f8c1c99eaa8c51109a6ca",
      "bytes": 622
    },
    {
      "path": "characters/Peng Cheolyeong.md",
      "sha256": "4b04778af1a227d6ed3af5e195faec3d97b8abd0e0238f570817bce78bdff5eb",
      "bytes": 679
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "9c75e253a29bf0acb6c26696af4bf9245e5744711704cfe44e4244a4729d0573",
      "bytes": 270550
    }
  ],
  "estimated_tokens": 11168
}
-->

# Durable State Update — Chapter 971

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
1 and safe_through 971. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 971. Profile updates may replace only one
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
  "chapter": 971,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 971,
    "continuity_sources": [971],
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
    "Jin Taekyung has returned after two years away with White Flame and intervened to save Jin Mukyung, Cheol Mubaek, and Wipeng.",
    "Jin Mukyung, Cheol Mubaek, and Wipeng are unconscious after the clash; their conditions are unknown.",
    "Murong Baek is the North Heaven Demon Lord and a Dark Heaven agent; he and an unidentified nomad face Taekyung in the gorge.",
    "Taekyung is severely exhausted after crossing ten thousand li without proper rest, meals, or time to circulate his qi.",
    "Two cutting whistles arrive after Taekyung says he brought someone with him; the companion's identity is unknown.",
    "Murong Baek betrayed Peng Cheolhu, who remains alive beneath the rubble; Murong intends to kill him.",
    "The Emperor remains gravely ill with Blood Soul Gu; treatment requiring him to die once remains unresolved."
  ],
  "continuity_sources": [
    969,
    970
  ],
  "open_questions": [
    "Who is the person Taekyung brought, and what do the two incoming attacks target?",
    "What are the conditions of Mukyung, Cheol Mubaek, and Wipeng?",
    "Who is the nomad accompanying Murong Baek, and how will the confrontation unfold?",
    "Can the Emperor be treated for Blood Soul Gu, and what does the treatment requiring him to die once entail?"
  ],
  "safe_through": 970,
  "temporary_decisions": [
    "Use “hyung” for 진태경’s address to his older brother."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 하북팽가   | **Hebei Peng Family**            |
| 무인     | **martial artist**                               | Default term                                          |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 가주     | **Family Head**                              |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 노부      | **this old man / I**                                            |
| 공자      | **Young Master**                                                |
| 철영 | **Cheolyeong** | Peng Cheolhu’s eldest son and the current Family Head of the Peng Family. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 팽철영 | **Peng Cheolyeong** | Family Head of the Hebei Peng Family and successor to the Thunderbolt Saber King. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 철혈도 | **Iron Blood Saber** | Epithet of Peng Cheolyeong. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 단환 | **pill** | A martial elixir in pill form; Mungyeong gives Taekyung a custom-made one. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 북천 | **North Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 케식 | **Keshik** | Elite warriors serving the Golden Clan. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 자무카 | 진무경 | hostile opponents | you | familiar, blunt, and patronizing | Jamukha uses 자네 while urging Mukyung to submit and become his hunting dog. |

## Listed compact profiles

### Cheolyeong.md

# Cheolyeong (철영)

- **Safe through:** Chapter 948
- **Aliases:** None
- **Role:** Cheolyeong is the current Family Head of the Peng Family in Hebei.
- **Personality:** Not established.
- **Voice:** Not established
- **Relationships:** He is Peng Cheolhu’s eldest son.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 970
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 944
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Jamukha.md

# Jamukha (자무카)

- **Safe through:** Chapter 969
- **Aliases:** None
- **Role:** Jamukha is the ruler of the western steppe and a former eastern-steppe chieftain recruited into Dark Heaven by Murong Baek.
- **Personality:** Patient and driven by a long-standing desire to avenge his defeat by Peng Cheolhu.
- **Voice:** Not established
- **Relationships:** Peng Cheolhu defeated him more than fifty years ago; Murong Baek spared him, recruited him into Dark Heaven, and commands him as a subordinate.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 968
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and says they have shared everything since he accepted him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 970
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Supreme Peak swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and guided by a strong sense of chivalry, refusing to abandon what he believes is right.
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, whom Mukyung loves and wanted to become a brother worthy of his pride.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 968
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and learning to trust his allies rather than carry every burden alone.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 968
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Peng Cheolyeong.md

# Peng Cheolyeong (팽철영)

- **Safe through:** Chapter 948
- **Aliases:** Iron Blood Saber
- **Role:** Family Head of the Hebei Peng Family; son and successor of the Thunderbolt Saber King.
- **Personality:** Calm and prudent under pressure, prioritizing consultation over risking his family’s lives on a hasty decision.
- **Voice:** He speaks calmly and deliberately, even when explaining grave decisions.
- **Relationships:** Son of the Thunderbolt Saber King; Jeok Cheongang says his past fight was followed by no further contact and that the Peng Family fabricated a later story about their encounter.

## Korean source

```text
＃971화



인간의 감각은 상상하는 것 이상으로 많은 정보를 제공한다.

범인들과는 비교조차 할 수 없을 만큼 오감이 발달한 무림인이라면 더더욱.

그리고 약육강식의 법칙 속에서 살아가는 그들은 혹독한 수련을 통해 예리하게 가다듬은 감각으로, 육안으로 확인할 수 없는 먼 곳에서 벌어지는 일들을 감지해 낼 수 있었다.

지금 북천마군이 그러하듯이.

“그래서, 겸사겸사 아는 사람 좀 데려왔지.”

열화신룡 진태경.

엄청난 기세로 등장한 것과는 달리, 지친 기색이 역력한 애송이의 여유로운 목소리를 듣자마자 북천마군의 머릿속에 붉은 경고등이 켜졌다.

자연스럽게 떠오른 누군가의 별호와 이름도 함께.

‘화왕(火王) 적천강.’

정사지간을 아우르는 거인이자, 구화산의 노괴.

그리고 태원진가의 망나니 삼공자를 제자로 거둔, 한 사람의 스승이기도 한 그를 떠올린 북천마군의 눈이 크게 뜨였다.

‘그렇다는 건.’

북천마군은 확신했다.

언제부터, 어디부터인지는 모르나 일이 틀어졌다는 것을.

비록 모든 계획이 생각대로 흘러가는 것은 아니라지만, 적어도 진태경과 적천강은 이 자리에 있어서는 안 되는 인물들이다.

‘정보가 새어 나갔군.’

그러나 그 생각이 누가, 어떻게, 라는 의문으로 이어지는 일은 벌어지지 않았다.

아니, 그럴 틈도 주지 않았다는 것이 정확한 표현이었다.

쉬익, 후우우웅!

하나는 은밀하면서도 쾌속하고, 또 다른 하나는 미친 듯이 휘몰아치는 광풍과도 같다.

이미 오감을 넘어 육감(六感)에 도달한 감각을 통해 전해지는 두 줄기의 파공성에, 북천마군은 미간을 좁혔다.

하나가 아닌 둘.

그것이 가진 의미는 크다.

파공성이 들려온 방향이, 정면의 지상이 아닌 좌우로 늘어선 암벽 위라는 사실보다도.

콰아아아앙!

삼십여 장이 넘는 아득한 높이의 암벽 위에서 울려 퍼지는 굉음.

여러 사람이 내지르는 끔찍한 비명이 뒤섞인 그것은 마치 천둥과도 같았다.

누군가의 생명을 집어삼키고, 때아닌 소나기를 부르는 천둥.

투둑. 투두둑.

북천마군의 곁에서 숨죽인 채 어둠에 잠긴 암벽 위를 올려다보던 자무카는, 불현듯 얼굴에 닿는 뜨거운 액체를 느낄 수 있었다.

붉고, 끈적한 핏물을.

“……!”

자무카의 입꼬리가 파르르 떨렸고, 북천마군의 눈빛은 침잠하게 가라앉았다.

두 사람 모두 이것이 의미하는 바를 알고 있었으니까.

전멸(全滅).

적지 않은 희생을 치르며 암벽 위로 올려보냈던 유목민들은 이제 없다.

촌각이라 부를 수조차 없을 만큼 짧은 시간 동안 모조리 죽음을 맞이했거나, 사로잡힌 것이 분명했다.

그리고 북천마군에게 있어 가장 중요한 것은, 단숨에 암벽 위를 휩쓸어 버린 두 괴물의 정체였다.

“하나는 당연히 네 스승일 테고, 다른 하나는 누구지?”

북천마군의 입술 사이로 흘러나온 건조한 음성에, 아직 설익은 젊은 괴물이 짐짓 준엄한 얼굴로 대답했다.

“어허, 스스로 알아낼 생각을 해야지. 가정 교육을 어떻게 받았길래 그 나이 처먹고 답안지부터 들춰 보려고 하나.”

북천마군은 순간 진태경의 머리통을 갈라서 들춰 보고 싶은 충동에 사로잡혔지만, 암벽 위의 괴물들은 그가 발걸음을 떼는 것조차 허락하지 않았다.

슈확!

비좁은 협곡 안이 환하게 물든다. 공간을 가로지르며 들이닥친 한 줄기의 섬광을 향해, 북천마군은 망설임 없이 손에 쥐고 있던 창을 휘둘렀다.

쾅!

날붙이끼리의 충돌이라고는 생각할 수 없는 굉음.

찰나의 격돌과 함께 튕겨 나가 지면 깊숙이 틀어박힌 섬광의 정체를 확인한 북천마군이 눈살을 찌푸렸다.

“돌격창?”

틀림없다. 그것은 초원의 유목민들이 사용하는, 흔하기 짝이 없는 형태의 돌격창이었다.

또한 동시에, 단순한 투창(投槍)의 수법이라고는 믿을 수 없을 만큼 쾌속한 일격이기도 했다.

마치, 누군가에 의해 쏘아진 화살처럼.

‘잠깐. 그렇다면 설마?’

북천마군은 불현듯 고개를 들었다.

그리고 때마침 흩어진 먹구름 사이로 비친 달빛 아래, 장창이라고 착각할 정도로 거대한 활을 든 한 여인을 볼 수 있었다.

“……궁성(弓星).”

신음처럼 흘러나온 뇌까림.

동시에 다시 한번 빗발치는 섬광.

콰아아아!

눈부신 속도로 움직이는 활시위와 함께 파공성이 울려 퍼진다.

십여 자루의 돌격창을 마치 화살처럼 가볍게 쏘아 보낸 궁성은, 천천히 힘을 주어 활시위를 당겼다.

우우웅.

파르르 떨리는 공간.

공력으로 이어진 은빛 선을 따라 응집한 휘황한 기운이 화살의 형태를 그려 내고, 이내 거대한 힘을 머금고 쏘아졌다.

북천마군이 아닌, 또 다른 적들을 향해.

화아아아악!

짙은 어둠이 찢어졌다.

전장의 모두가 그 눈부시도록 파괴적인 섬광을 볼 수 있었다.

쉰 목소리로 끊임없이 함성을 내지르며 협곡 안의 적들을 베어 넘기던 산서인들도.

그런 그들에 의해 속절없이 죽음을 맞이하던 유목민들도.

그리고 협곡 너머의 너른 분지에서, 유목민들과 모용세가에 포위당한 채 힘겨운 전투를 이어 나가고 있던 하북팽가의 무인들도.

“저게 도대체 뭐…….”

뒤늦게 허공에서 쏟아지는 십여 줄기의 섬광을 발견한 케식 백인장은 꿈에도 알지 못했다.

지금 막 제 입술 사이로 흘러나온 의문 어린 목소리가, 곧 그의 유언이 되리라는 것을.

더불어 그를 비롯한 수백여 명의 아군이 이승에서 보는 마지막 광경이 되리라는 것을.

콰아아앙!

무시무시한 굉음과 함께 땅이 뒤집힌다.

주인을 알 수 없는 피 분수와 함께 솟구친 누군가의 팔과 다리가, 혹은 형체조차 제대로 남기지 못한 살점과 내장 조각이 사방으로 비산했다.

콰드드득, 철퍽.

뒤늦게 지면 위로 떨어진 핏물과 살점들이 모두의 귓가를 파고든다.

생각지도 못한 모용세가의 배신으로 사방을 포위당한 채 피투성이가 되어 가고 있던 하북팽가의 가주, 철혈도(鐵血刀) 팽철영은 멍하니 눈을 깜빡였다.

‘지금, 무슨 일이 벌어진 거지?’

협곡을 등진 채 수십여 명의 적들을 단신으로 상대하던 그는 미처 보지도 못했다.

그저 문득 하늘이 밝아졌다고 느꼈고, 등골이 오싹해지더니 본능적으로 손이 멈췄다.

그리고…… 그리고 그것이 전부였다.

눈동자를 찌르는 휘황한 빛에 눈을 감았다 뜨자, 사방을 가득 메우고 있던 적들은 사라져 있었다.

아니, 정확히 표현하자면 그들은 여전히 그 자리에 남아 있었다.

더는 인간이라 부를 수 없는 형태로.

상반신이 사라지거나, 팔다리가 뜯겨 나간 채로.

“으어, 으아아아!”

“크아아아악!”

고통을 가장 먼저 받아들이는 것은 몸이지만, 고통은 인지하는 것은 두뇌다.

뒤늦게 이 믿기지 않는 현실을 인지한 그들은 처절한 비명을 토해 냈다.

섬광에 휩쓸려 목숨을 잃은 수백여 명과는 달리 운 좋게 살아남은 생존자들은 엄습하는 고통에 몸부림쳤고, 모두를 얼어붙게 한 끔찍한 비명이 잦아들기도 전에 다시 한번 하늘이 환하게 물들었다.

화아아악.

그 순간, 팽철영은 깨달았다.

평소였다면 넋 놓고 바라보았을 저 눈부신 빛줄기가, 곧 죽음을 의미한다는 것을.

더불어 그 죽음이, 자신을 비롯한 하북팽가의 무인들에게는 해당되지 않는다는 사실을.

“쳐라-!”

공포는 전염되고, 희망은 타오른다.

피와 시체로 뒤덮인 분지 위를 환하게 물들이는 섬광을 등진 채, 하북팽가의 무인들은 이미 허물어진 포위망을 갈기갈기 찢어 부수며 나아갔다.

전장에 선 모두가 들을 수 있을 만큼 맹렬한 함성과 함께.

저 멀리, 비좁은 협곡 깊은 곳까지 쩌렁쩌렁하게 울려 퍼질 정도로.

“듣기 좋네. 물론 당신한테는 아니겠지만.”

북천마군은 웃고 있는 진태경의 얼굴을 말없이 바라보았다.

익살스러운 목소리와는 달리, 깊게 가라앉아 있는 어린놈의 눈동자에 비친 자신의 얼굴은 딱딱하게 굳어 있었다.

‘궁성이라니.’

그녀의 존재만큼은 미처 예상치 못했다.

이 자리에 나타나기에는 너무나도 오래된 과거의 망령이었으니.

“여유를 부린 이유가 있었군.”

짧은 침묵 끝에 흘러나온 한마디. 그와 함께 이제야 대략적인 정황을 깨달은 북천마군이 문득 입을 열었다.

“그래, 황궁이었나.”

궁성의 등장과 함께 흩어져 있던 머릿속 실마리가 이어진다.

진태경이 이곳에 나타날 수 있었던 이유. 암천이 황도를 중심으로 펼친 계획의 성공 유무.

마지막으로 홀연히 자취를 감추었던 궁성이 어디에 몸을 의탁하고 있었는지도.

“하지만, 어떻게 이토록 빠르게 알아차린 거지?”

북천마군이 불쑥 던진 물음에, 진태경이 대답했다.

“네 친구가 알려 주던데.”

“친구?”

“동천마군(東天魔君).”

“……!”

“그러니까 평소에 좀 친하게 지내지 그랬냐. 같이 밥도 자주 먹고, 강호의 도리에 따라 품번도 공유하고. 뭐, 나야 더 늦기 전에 알았으니 천만다행이었지만.”

밉살맞은 표정으로 어깨를 으쓱한 진태경이 덧붙였다.

“잠시 후에 만나면 나 대신 감사 인사나 전해 줘. 죽어 마땅한 놈이긴 했는데 마지막에는 조금 신경 쓰이더라고.”

그 말에 담긴 의미를 알아들은 북천마군이 고소를 머금었다.

“정중하게 거절하도록 하지.”

“왜, 그 정도까지 사이가 안 좋아? 혹시 예전에 삼각관계였나?”

“미친놈. 도무지 혓바닥이 쉬지를 않는군.”

“안 그래도 슬슬 그만할 생각이야. 이제는 몸도 좀 움직일 만하고.”

진태경의 입가에 맺혀 있던 미소가 흐릿해졌다.

지칠 대로 지친 상황 속, 진무경을 구하기 위해 혼신의 힘을 다해 쏘아 보냈던 일격으로 비롯된 탈력감은 이미 가라앉힌 후였다.

“고맙다. 숨 고를 때까지 기다려 줘서.”

그런 진태경을, 북천마군은 가라앉은 눈빛으로 바라보았다.

애초에 스스로의 의지로 시간을 내어준 것이 아니라, 또 다른 누군가에 의해 내어줄 수밖에 없었던 것이었으니까.

“이제 그만하고 나오지 그러나, 화왕.”

텅 빈 허공을 향한 북천마군의 한 마디에, 어둠 속에 녹아들어 있던 인영이 부드럽게 떨어져 내렸다.

“안타깝군. 한 발자국이라도 뗐으면 네놈의 사지를 불태워 버렸을 텐데.”

“글쎄, 과연 그럴 수 있을까.”

북천마군은 대답과 함께 창 자루를 비스듬히 움켜쥐었다.

오래전에 흘러가 버린 아득한 과거, 전장에서 마주친 적 있던 적천강의 기억 속에서는 찾아볼 수 없는 미증유(未曾有)의 기운이 창날을 타고 솟구쳤다.

“많이 컸구나. 하룻강아지 주제에 노부의 앞에서 반말이나 찍찍 싸며 배짱도 부릴 줄 알고.”

적천강은 이빨을 드러내며 웃었다. 활짝 펼쳐진 그의 양손을 타고 백색의 겁화가 넘실거렸다.

“언제부터였느냐. 놈들과 손을 잡은 것이.”

“희한한 일이군. 견원지간(犬猿之間) 같던 두 사람이, 오늘 이 자리에서 똑같은 질문을 하다니.”

그 순간, 적천강은 입가의 미소를 지웠다.

지금 북천마군이 누구를 말하는지, 그리고 그의 목숨이 경각에 달해 있다는 사실을 알고 있기 때문이었다.

“……제자 녀석이 팽가 놈에게 큰 빚을 졌으니, 네놈의 목숨으로 갚아야겠군.”

“두 사람이 함께 떠나게, 저승으로.”

북천마군은 담담한 대답과 함께, 손에 쥐고 있던 것을 입안에 털어 넣었다.

스륵.

혀를 타고 녹아드는 붉은 색의 단환. 동시에 그의 등 뒤에서 진태경의 창날이 번뜩였다.
```

## Final English reading copy

```markdown
# Chapter 971

Human senses provide far more information than you might imagine.

That was especially true of martial artists, whose five senses were incomparably sharper than those of ordinary people.

Living by the law of the jungle, they honed those senses through brutal training until they could detect events unfolding far beyond what the naked eye could see.

Just as the North Heaven Demon Lord did now.

“So, while I was at it, I brought someone I know.”

Jin Taekyung, the Blazing Flame Divine Dragon.

The moment the North Heaven Demon Lord heard the easygoing voice of the young upstart, who looked plainly exhausted despite the overwhelming force of his arrival, alarm bells went off in his head.

Along with it came the title and name of someone who naturally sprang to mind.

*The Fire King, Jeok Cheongang.*

A giant who straddled the orthodox and unorthodox factions, an old monster of Mount Jiuhua.

And a master, too—the man who had taken the wastrel Third Young Master of the Jin Family of Taiyuan as his Disciple.

The North Heaven Demon Lord’s eyes widened as he thought of him.

*If that’s the case…*

The North Heaven Demon Lord was certain.

He didn’t know when or where things had gone wrong, but something had.

Not every plan went exactly as intended. Still, at the very least, Jin Taekyung and Jeok Cheongang were not supposed to be here.

*The information leaked.*

But that thought never led to the question of who had leaked it, or how.

No—that wasn’t quite right. He hadn’t even been given the chance to wonder.

*Whoosh! Whoooooom!*

One sound was quiet yet swift. The other was like a furious gale, whirling out of control.

The two streaks of sound reached him through senses that had gone beyond the five and touched the sixth. The North Heaven Demon Lord furrowed his brow.

Not one. Two.

That meant something.

More than the fact that the sounds had come from the cliffs to either side, not from the ground ahead.

*KABOOOOOM!*

A thunderous crash rang out from the top of the cliffs, more than thirty *zhang* high.

Mixed with it were the horrific screams of many people. It sounded like thunder.

Thunder that swallowed someone’s life and summoned an untimely shower.

*Drip. Drip-drip.*

Jamukha, who’d been standing beside the North Heaven Demon Lord, silently looking up at the shadowed cliff, suddenly felt a hot liquid touch his face.

Red, sticky blood.

“……!”

Jamukha’s lips trembled. The North Heaven Demon Lord’s gaze sank, dark and still.

They both knew what it meant.

Annihilation.

The nomads they’d sent up the cliff at considerable cost were gone.

They had all been killed or captured in less time than it took to blink.

And the most important thing to the North Heaven Demon Lord was the identity of the two monsters who’d swept across the cliff in an instant.

“One of them is obviously your master. Who’s the other?”

At the North Heaven Demon Lord’s dry question, the young monster—still a little green—put on a stern expression and replied.

“Now, now. You should figure it out for yourself. What kind of upbringing did you have, asking to peek at the answer sheet at your age?”

For a moment, the North Heaven Demon Lord felt an urge to crack open Jin Taekyung’s skull and see what was inside. But the monsters on the cliff wouldn’t even let him take a step.

*Shwaa!*

The narrow gorge lit up. The North Heaven Demon Lord swung the spear in his hand without hesitation toward a streak of light hurtling through the air.

*BOOM!*

The crash was too loud to have come from two metal blades clashing.

The flash ricocheted from the impact and buried itself deep in the ground. The North Heaven Demon Lord frowned as he recognized it.

“A charging spear?”

No doubt about it. It was the most ordinary sort of charging spear used by the nomads of the steppe.

And yet the strike had been so swift it was hard to believe it was a simple throw.

Like an arrow shot by someone.

*Wait. Then could it be…?*

The North Heaven Demon Lord suddenly looked up.

Just then, moonlight slipped through the scattered clouds, revealing a woman holding a bow so enormous it could have been mistaken for a long spear.

“……The Bow Saint.”

The words left his lips like a groan.

At the same moment, flashes rained down once more.

*KABOOOM!*

The bowstring moved too fast to follow, and the sound of its release rang through the gorge.

The Bow Saint had fired more than ten charging spears as lightly as arrows. Now she slowly pulled the bowstring back, gathering her strength.

*Wooooom.*

Space trembled.

Along a silver line formed from internal energy, a brilliant mass of power took shape like an arrow. Then it shot forth, carrying immense force.

Not toward the North Heaven Demon Lord, but toward the other enemies.

*FWOOSH!*

The deep darkness tore open.

Everyone on the battlefield could see that dazzlingly destructive flash.

The Shanxi martial artists, hacking their way through the enemies in the gorge with hoarse, unrelenting battle cries.

The nomads being slaughtered helplessly by them.

And the martial artists of the Hebei Peng Family, fighting desperately in the broad basin beyond the gorge while surrounded by nomads and the Murong Family.

“What in the world is that—”

The Keshik centurion had only just spotted the dozen or so streaks of light raining down from the sky. He had no idea that the bewildered words leaving his lips would soon be his last.

Nor that those streaks of light would be the last thing he and hundreds of his comrades saw in this world.

*KABOOOOOM!*

The earth turned over with a terrifying crash.

Someone’s arms and legs shot up amid fountains of blood. Flesh and pieces of organs—some so mangled they were barely recognizable—flew in every direction.

*Krrrsh. Splatter.*

Blood and flesh pattered down onto the ground, their late arrival ringing in everyone’s ears.

Peng Cheolyeong, Family Head of the Hebei Peng Family and the Iron Blood Saber, had been covered in blood, surrounded on all sides because of the Murong Family’s betrayal. He blinked blankly.

*What just happened?*

With his back to the gorge, he’d been fighting dozens of enemies alone. He hadn’t seen a thing.

He’d only felt the sky brighten. A chill had run down his spine, and his instincts had made his hand stop.

And… and that was all.

When he shut his eyes against the dazzling light stabbing into them, then opened them again, the enemies that had filled the area had vanished.

No. To be precise, they were still there.

Just no longer in a shape that could be called human.

Some had lost their upper bodies. Others had been torn apart, limbs missing.

“Ugh—aaah!”

“Graaaah!”

The body feels pain first, but the brain is what understands it.

Only when they grasped the unbelievable reality did the survivors let out desperate screams.

Unlike the hundreds swept away by the flash, those lucky enough to survive writhed in pain. Before the horrific screams that had frozen everyone in place could die down, the sky lit up once more.

*FWOOSH.*

In that moment, Peng Cheolyeong understood.

That dazzling beam of light—which he would normally have stared at in a daze—meant death.

And that death was not meant for him or the martial artists of the Hebei Peng Family.

“Attack!”

Fear is contagious. Hope catches fire.

With the brilliant flash over the basin of blood and corpses behind them, the martial artists of the Hebei Peng Family surged forward, ripping apart the encirclement that had already crumbled.

Their fierce cries rang out loudly enough for everyone on the battlefield to hear.

Loud enough to echo all the way into the depths of the narrow gorge in the distance.

“Sounds nice. Not for you, though.”

The North Heaven Demon Lord silently watched Jin Taekyung’s smiling face.

The young bastard’s eyes were deep and steady, despite his mischievous voice. In them, the North Heaven Demon Lord saw his own face, stiff with tension.

*The Bow Saint.*

He hadn’t anticipated her presence.

She was a ghost from the distant past, far too long gone to appear here.

“So that’s why you were so relaxed.”

After a brief silence, the North Heaven Demon Lord finally spoke. It seemed he’d pieced together the general situation.

“So it was the Imperial Palace.”

With the Bow Saint’s appearance, the scattered threads in his mind came together.

Why Jin Taekyung could have appeared here. Whether Dark Heaven’s plan centered on the Imperial Capital had succeeded.

And finally, where the Bow Saint had been staying after vanishing without a trace.

“But how did you figure it out so quickly?”

Jin Taekyung answered the North Heaven Demon Lord’s sudden question.

“Your friend told me.”

“My friend?”

“The Eastern Heaven Demon Lord.”

“……!”

“So you should’ve been a little friendlier. Had meals together more often, swapped catalog numbers like any upstanding members of the martial world. Well, I’m just glad I found out before it was too late.”

Jin Taekyung shrugged with an obnoxious look, then added:

“When you see him in a bit, thank him for me. He deserved to die, but at the end, I found myself a little concerned about him.”

The North Heaven Demon Lord understood what he meant and smiled bitterly.

“I’ll have to politely decline.”

“What, were you two really that unfriendly? Were you in a love triangle or something?”

“Crazy bastard. Does your tongue ever get tired?”

“I was about to stop anyway. I can move a little now.”

The smile lingering on Jin Taekyung’s lips faded.

He had already shaken off the weakness left by the strike he’d launched with all his strength to save Jin Mukyung, exhausted as he was.

“Thanks. For waiting until I caught my breath.”

The North Heaven Demon Lord looked at him with a subdued gaze.

He hadn’t given Jin Taekyung time of his own accord. He’d simply had no choice, because someone else had forced him to.

“Enough of this. Why don’t you come out now, Fire King?”

At the North Heaven Demon Lord’s words, addressed to empty air, a figure that had blended into the darkness drifted gently down.

“What a shame. If you’d taken even one step, I’d have burned your limbs off.”

“I wonder if you really could.”

As he replied, the North Heaven Demon Lord gripped his spear at an angle.

From the spearhead surged an unprecedented power—one that Jeok Cheongang had never sensed in the distant past, when they’d faced each other on the battlefield.

“You’ve grown bold, haven’t you? A mere pup, speaking to this old man like an equal and even daring to act tough.”

Jeok Cheongang grinned, baring his teeth. White hellfire rippled over his outstretched hands.

“When did you start working with them?”

“What a strange thing. The two of you, who were like cats and dogs, asking me the same question here today.”

At that moment, the smile disappeared from Jeok Cheongang’s lips.

He knew whom the North Heaven Demon Lord meant—and that his life was hanging by a thread.

“……My Disciple owes the Peng bastard a great debt. I’ll repay it with your life.”

“You’ll both be going together—to the afterlife.”

The North Heaven Demon Lord replied calmly, then tossed what he was holding into his mouth.

*Slip.*

A red pill melted across his tongue. At the same time, Jin Taekyung’s spearhead flashed behind him.
```
