<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1054.txt",
      "sha256": "8c4a8a50f92860d19c0ac51e110ba83cc205918473e804e808fa3c9a17eb4526",
      "bytes": 12507
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3b6625408003974333bf4a24c059d5d2f636d5eef081104c1b2e5ee2fcbe909f",
      "bytes": 1137
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "91edff1ea0e7f2d1bdf20f77998a86f250b89f1bc3f043cd106289bea1e118b4",
      "bytes": 240895
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "83d813a9c449ea8b3873b746447cab40016a73514d4eb476ff6dd94227ce3597",
      "bytes": 920
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1d05a6e2a8a554058f349ca361bd8e2808cb4e75216c54c99226f584609849f5",
      "bytes": 760
    },
    {
      "path": "characters/Hwangbo Eom.md",
      "sha256": "878117b61e6b852f1ba4f3810f8e0cee4523ae280c512250c7303054a0acca1a",
      "bytes": 674
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6d493822f42dcf3ef6207c09e15c4347c6a34ab4d314cf317aa5bf990eb5f0c1",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "9da53c33d5319c0c04a51878a74ae8b882faba8fa6f21aac8126fb475caf51c6",
      "bytes": 623
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "64f1789f77672b68330e3eff69e4ebc0c9251efbedf3de57e2c57bc7502b5bdc",
      "bytes": 800
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "c6cd7845d6dc2ffbee4f07de43a11f1316c1acf8fa25f1b54e2e298562c7d7a9",
      "bytes": 774
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e476e49cdcddf6de4980fb9437ae78bed54ffc02a595fe7c61e28608999f8e34",
      "bytes": 281989
    }
  ],
  "estimated_tokens": 10640
}
-->

# Durable State Update — Chapter 1054

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
1 and safe_through 1054. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1054. Profile updates may replace only one
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
  "chapter": 1054,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1054,
    "continuity_sources": [1054],
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
    "The Grand Mage survived Teleport and reached allies at an unknown location.",
    "Jin suspects a connection between the Lord of Heaven and the dead Demon King, Asmodeus; the truth is unknown.",
    "The battle below the hill continues as a force of thousands arrives, shifting its balance.",
    "An unknown person prepared the battle’s stage from thousands of ri away."
  ],
  "continuity_sources": [
    1052,
    1053
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Why does the Lord of Heaven want Jin to survive and grow stronger?",
    "Are the Lord of Heaven and Asmodeus connected?",
    "Who prepared the battle’s stage, and why?"
  ],
  "safe_through": 1053,
  "temporary_decisions": [
    "Render 대마도사 and 대술사 as Grand Mage.",
    "Use Fire Ball, Stone Wall, and Magic Arrow for the named spells.",
    "Render 헬 파이어 as Hell Fire; use hellfire for descriptive 겁화.",
    "Render 쇄월검진 as Moon-Shattering Sword Formation.",
    "Render the achievement 배 째 as “Go Ahead, Gut Me!”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 송일     | **Song Il**        |
| 사마공    | **Sima Gong**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 암천     | **Dark Heaven**                  |
| 장문인    | **Sect Leader**                              |
| 산서     | **Shanxi**             |
| 청해     | **Qinghai**            |
| 귀가      | **your family**                                                 |
| 도사      | **Daoist**                                                      |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 황보엄 | **Hwangbo Eom** | Personal name of the Taeeul Merciless Sword. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 잠룡 | **Hidden Dragon** | Epithet or metaphor for Jin Taekyung. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 황보 | **Hwangbo** | Surname form used when addressing Hwangbo Eom. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 심맥 | **heart meridian** | Meridian severed by an infiltrator to commit suicide. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 돈황 | **Dunhuang** | City identified as the foremost defensive line in Gansu. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 진태경 | 황보엄 | junior_martial_artist_to_Zhongnan_senior | Great Hero Hwangbo | casual-polite and teasing | Taekyung uses 황보 대협 after deliberately pretending not to recognize Hwangbo. |
| 황보엄 | 진태경 | Zhongnan_senior_to_younger_martial_artist | insolent brat | blunt, amused, and probing | Hwangbo describes Taekyung as a 건방진 아해 and later treats him as a youngster. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 진태경 | 사마공 | allied young martial artist to unorthodox sect leader | Great Hero Sima | polite and deferential | Addresses him as 사마 대협. |
| 사마공 | 진태경 | unorthodox sect leader to celebrated young martial artist | you | polite and familiar | Uses 자네 while speaking to Taekyung. |
| 혈검마군 | 진태경 | enemy addressing a younger martial artist | you | familiar and measured | Uses 자네 while praising and assessing Taekyung. |
| 진태경 | 혈검마군 | young martial artist confronting an enemy | you | casual and challenging | Questions when the Blood-Sword Demon Lord and the Lord of Heaven appeared. |
| 혈검마군 | 천주 | servant_to_master | Lord of Heaven | deferential | In his inner monologue, he addresses his absent master as 당신 and refers to himself as 속하. |
| 송일 | 황보엄 | Senior Brother to Junior Brother | Junior Brother | familiar and heated | Song Il calls Hwangbo Eom 사제. |
| 황보엄 | 송일 | Junior Brother to Senior Brother | Senior Brother | familiar and dryly teasing | Hwangbo Eom calls Song Il 대사형. |
| 혈검마군 | 사마공 | former bargaining allies turned enemies | you; you traitor | blunt and hostile | Uses direct, contemptuous forms while accusing Sima Gong of betraying him. |
| 사마공 | 혈검마군 | former bargaining allies turned enemies | you; you Demonic Cult bastard | calm and contemptuous | Uses 당신 before ending with the insult 마교 잡놈아. |
| 대술사 | 혈검마군 | subordinate_to_commander | Demon Lord | respectful and formal | Addresses him as 마군 while acknowledging his injuries. |
| 혈검마군 | 대술사 | commander_to_subordinate | Grand Mage | blunt and commanding | Orders her to heal him immediately. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1052
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Devoted to his master and proud of his abilities, he is deeply wounded by perceived distrust and resolves to prove his worth.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He serves the Lord of Heaven with deep devotion, but the Grand Mage says the Lord ordered his disposal; he has been ordered not to kill Jin Taekyung, admires Jeok Cheongang, and once shared the Demonic Cult with the fiends who became Black Ghosts.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1053
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hwangbo Eom.md

# Hwangbo Eom (황보엄)

- **Safe through:** Chapter 1052
- **Aliases:** Taeeul Merciless Sword
- **Role:** Supreme Peak master of the Zhongnan Sect and its Second Martial Uncle, known as the Taeeul Merciless Sword.
- **Personality:** Ruthless, severe, proud, and deeply invested in restoring Zhongnan's standing.
- **Voice:** Calmly courteous when offering tea, then cold, commanding, and cutting when reprimanding others.
- **Relationships:** Song Il and Hwangbo Eom are Gong Iljung’s two Senior Brothers; the three served the same Master for over fifty years, and Hyuk Sopyung is Hwangbo’s junior.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1053
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1053
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1052
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet capable of risking himself for a moment of conscience, he values his heir’s future and repaying a debt to Jeok Cheongang.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he aided Jeok Cheongang despite their history, and hopes his heir will carry on the Black Dragon Demon Gate.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1052
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant and domineering, but capable of remorse over choices that harmed his sect and those he failed to protect.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

## Korean source

```text
＃1054화



- 깨어나라.

그 이상의 무언가는 필요하지 않았다.

수면 밑으로 잠겨가던 정신을 일깨우고 뇌리를 지배하는 짧은 속삭임에, 조금의 미동도 없이 굳게 닫혀 있던 눈꺼풀이 열렸다.

“아.”

짧은 탄성과 함께 토해진 숨결.

마침내 의식을 되찾은 여인, 대술사는 사방을 짓누르고 있는 칠흑 같은 어둠을 보며 비로소 깨달았다.

마지막 순간, 위험을 무릅쓰고 던진 도박수가 성공했다는 사실을.

그리고 죽음에 이를 정도의 치명상을 입은 자신이 이처럼 살아있을 수 있는 이유를.

“천상천하(天上天下), 만마앙복(萬魔仰伏)!”

영혼에 새겨진 여덟 글자의 교언(敎言)을 쏟아낸 대술사는 황급히 짙은 어둠을 향해 엎드렸다.

먼저 두 무릎을 꿇고, 이어 두 팔을 땅에 대고, 마지막으로 소리가 울리도록 이마를 찧으면서.

쿵, 쿵, 쿵.

아릿한 통증과 함께 차가운 석재 바닥 위로 핏방울이 떨어졌으나, 대술사는 아랑곳하지 않았다.

지금처럼 오체투지(五體投地)가 가능한 것도, 불안정한 공간에 휩쓸려 사라진 팔과 다리를 되찾을 수 있었던 것도 전부 한 존재가 내린 은혜 덕분이었으니까.

“어리석고 미천한 종복이, 위대하신 천주(天主)를 배알 하나이다.”

지극한 공경이 담긴 대술사의 음성에, 사방을 둘러싼 어둠이 느릿하게 일렁였다.

- 고하라. 네가 보고 들은 모든 것을.

머릿속에서 울려 퍼지는 짤막한 한 마디.

그러나 자신의 주인이 전투의 승패 따위를 묻는 것이 아니라는 사실을, 대술사는 누구보다 잘 알고 있었다.

주인의 관심은 오직 한 사람을 향해 쏠려 있었으니.

“천주께서 명하신 바를 목숨 바쳐 이루고자 했나이다.”

대술사는 감히 얼굴조차 들지 못한 채 말을 이었다.

진태경에게 희생당한 아군의 숫자가 대략 어느 정도인지, 또한 그러한 과정 속에서 몇 기의 흑귀가 쓰러졌고, 처음부터 마지막까지 펼쳐진 전황은 어떠했는지.

“하여, 부끄럽지만 이리 급히 몸을 피할 수밖에 없었습니다. 부디 죽여 주시옵소서.”

말을 끝마친 대술사는 조용히 입술을 깨물었다.

그녀로서는 최선을 다했으나, 모든 것이 계획대로 완벽하게 흘러간 것은 아니었으니까.

그리고 이러한 대술사의 두려움 속에서, 다시 한번 머릿속이 울렸다.

- 혈검(血劍)의 목숨을 취하는 것을 보지 못했다고?

“……예. 더불어 종남의 두 도사와 사마공이 재차 배반할 것을 예측하지 못했으니, 입이 열 개라도 드릴 말씀이 없나이다.”

혈검마군과 손을 잡고 있었던 흑야왕 사마공.

거기에 더해 그가 끌어들인 노호검객 송일과 태을무정검 황보엄까지.

정작 흑야왕을 시작으로 배신자들을 포섭한 혈검마군은 까맣게 몰랐지만, 본래의 계획대로라면 그들 모두가 진작 죽었어야 했다.

그것도 본격적인 전투가 시작되기 전에, 바로 진태경에 의해서.

“한데, 그 이전에 생각지도 못한 부분에서 일이 틀어졌습니다.”

- 무엇이더냐.

“공동(崆峒)입니다.”

공동파.

대술사가 계획한 이 무대의 첫 조연은 바로 그들이었다.

돈황에서 패주한 공동파의 생존자들은 후방의 아군과 합류하여 자신들이 보고 들은 모든 사실을 상세하게 밝혀야 했다.

암천이 보유한 엄청난 전력과 마법이라는 기이한 힘.

마지막으로 배신자들의 존재가 드러날 결정적인 의심의 싹을 틔우는 것이 대술사의 의도였다.

“하여, 그들의 귀에 닿을 수 있도록 배신자들에 관한 말을 흘렸습니다. 그리고 찾지 못한 척 놓아주었지요.”

처음부터 놓친 것이 아니다.

놓아주었다. 그것도 일부러.

구파일방의 일익인 공동파를 향한 것이라고는 믿을 수 없을 정도로 광오한 발언이었지만, 대술사는 지금까지도 확신하고 있었다.

만약 자신이 휘하에 거느린 술사들과 함께 살생을 목적으로 추격에 가담했다면, 공동파는 돈황에서 멸문(滅門)했을 것이라고.

하지만 대술사는 구태여 그들을 잡아 죽이지 않았다.

혈검마군과 달리 그녀의 목적은 승리가 아니었으니까.

그녀가 천주에게 따로 하달받은 명령은 오직 진태경의 생존과 성장뿐이었으니까.

그렇기에 공동파는 일부나마 살아남을 수 있었다.

장문인을 포함한 그들이 끈질긴 추격을 뿌리치고 포위망을 벗어났다는 소식을 들었을 때, 대술사는 혈검마군의 이목을 피해 웃음을 삼키며 이후의 일을 생각하고 있었다.

살아 돌아온 생존자들로 인해 모든 진실이 드러나고, 소수의 배신자들을 처단한 진태경이 적들의 새로운 구심점이 되어 전투에서 대승을 거두는.

실로 안전하고도 완벽한 계획을.

하지만…….

“진실을 알고 있던 공동파 장문인을 포함한 일부 생존자들이 자취를 감추었습니다.”

그 순간, 어둠이 크게 일렁였다.

- 자취를 감추었다?

“예. 송구하오나 이 종복에게 내려 주신 술법의 힘으로도 찾을 수 없었습니다. 그들은 어느 순간, 짐작할 수 없는 어딘가로 사라지고 말았습니다.”

생각지도 못한 첫 번째 균열이 발생했지만, 대술사로서도 그들의 흔적을 뒤쫓을 수는 없었다.

그렇게 시간이 흐르고, 본격적인 전투가 시작되었으며, 새로운 균열이 잇따라 생겨났다.

무슨 이유에선지 불리한 전황 속에서도 다시 한번 어리석은 길을 택한 배신자들.

스스로 심맥을 끊어 목숨을 건 도박을 감행한 진태경.

그리고 화왕과 궁성의 합류로 되려 위기에 처하게 된 대술사 자신까지.

“천명(天命)을 제대로 이행하지 못한 이 미천한 종복을, 부디 벌하여 주시옵소서.”

비록 소기의 목적은 달성할 수 있었으나 겨우 그뿐.

대술사는 더욱 깊이 고개를 떨구었다.

곧 천지를 떨어 울릴 주인의 진노를 기다리며.

그러나 그런 우려와 달리, 다음 순간 머릿속 깊은 곳에서 공명하듯 울려 퍼진 심언(心言)은 여느 때와 같이 무감정했다.

- 고개를 들어라.

대술사는 홀린 듯이 그 명령을 따랐다. 촘촘한 면사 너머로 살아 있는 것처럼 꿈틀거리는 어둠이 보였다.

지난 수십여 년을 통틀어, 그 어느 때보다 깊고 짙어진 어둠이.

- 보이느냐, 느껴지느냐.

대술사는 주인의 물음에 대답하지 않았다.

아니, 대답할 수 없었다.

어둠을 대면함과 동시에 새하얗게 뒤집혔던 동공이, 어느덧 검게 물들어 가고 있었으니까.

- 내게는 보인다. 느껴진다. 네 안에 숨어 있는 그 모든 것이. 선명하게.

솨아악.

망막을 완전히 잠식한 어둠은 거기에서 멈추지 않고 계속해서 뻗어 나갔다.

더욱 빠르게, 보다 깊숙이.

이지를 상실한 채 가냘픈 체구를 떨고 있는 충성스러운 종복의 마음을 지배하고, 뇌리를 휩쓸며, 심령(心靈)을 뒤흔든 끝에야 주인을 향해 되돌아갔다.

마치, 아무 일도 없던 것처럼.

털썩.

“어흡, 허억. 헉!”

어둠이 빠져나간 눈동자에 초점이 되돌아온 순간, 실이 끊긴 인형처럼 쓰러진 대술사는 가쁘게 숨을 헐떡였다.

“처, 천주시여.”

잘게 떨리는 목소리와 두려움 가득한 눈빛.

대술사는 본능적으로 알 수 있었다.

조금 전, 천주가 자신의 모든 생각과 기억을 읽고 들여다보았다는 사실을.

그와 동시에 소름이 끼칠 정도의 경외심이 찰나의 두려움을 밀어내고 그녀의 전신을 휘감았다.

‘이건…….’

자신의 육신에 스며들고 혼백(魂魄)을 사로잡았던 그 힘을 떠올리며, 대술사는 몸을 잘게 떨었다.

그것이 단지 자그마한 힘의 편린(片鱗)에 불과하다는 사실을 알고 있기에, 그녀가 느끼는 경이로움과 충격은 더욱 클 수밖에 없었다.

‘도대체 저분의 한계는 어디까지란 말인가.’

천년 묵은 고목이라 할지라도 구름에 닿을 수는 없는 법.

하지만 천주는 달랐다.

처음 대면했던 그 순간부터 절대자나 다름없던 그는, 한계라는 단어를 무색하게 만들 정도로 나날이 강해지고 있었다.

가장 가까운 심복 중 하나인 대술사가 경악할 정도로.

그리고 그녀는 이와 같은 믿을 수 없는 변화가 어디에서부터 시작되었는지, 이미 마음속으로 짐작하는 바가 있었다.

‘진태경. 아니, 선택받은 자.’

틀림없다.

불과 이년 남짓한 과거, 산서성에 피바람이 몰아치고 잠룡(潛龍)이라는 별호가 천하에 알려질 무렵부터 그녀의 주인에게도 변화가 생겨났으니까.

길게는 십 년, 짧아도 일 년 가까이 이어졌던 깊은 잠에서 자주 깨어났고 그때마다 대술사는 더욱 강력해진 천주의 힘을 느낄 수 있었다.

심지어 오늘 이 자리에서조차도.

‘하지만, 그것과 도대체 무슨 연관이……?’

자연스럽게 이어진 의문.

하지만 다음 순간 머릿속을 뒤흔드는 천둥 같은 울림에, 그녀의 뇌리가 새하얗게 물들었다.

- 그 어떠한 의문도, 너의 몫이 아니다.

“……!”

- 잊지 말라. 네 주인이 무엇을 원하는지. 네가 무엇을 해야 하는지.

마치 영혼을 관통하는 듯한 천주의 음성에, 대술사는 잠시 잊고 있던 사실을 깨달았다.

눈앞의 존재는 그야말로 모든 것을 초월한 절대자라는 사실을.

그를 주인으로 모시고 섬김에 있어, 그 어떤 의문이나 불신은 용납할 수 없다는 것을.

“부디, 부디 이 불경한 종복을 죽여 주시옵소서!”

대술사는 피를 토하듯 부르짖었다.

차가운 석재 바닥과 한 몸이 될 것처럼 엎드린 채, 광신(狂信)이라 부를 만한 충성심을 되새기며 주인을 찬양했다.

은방울 소리처럼 맑고 침착하던 목소리가 온통 쉬고 갈라질 때까지.

감히 잠시나마 의문을 품은 미천한 종복에게, 주인의 하교(下敎)가 내려올 때까지.

- 그만.

스륵.

일순간 부드럽게 일렁인 어둠이 대술사를 휘감았다.

마치 그녀를 다정하게 어루만지듯이.

- 그런 일은 결코 벌어지지 않을 것이다. 네 주인은 알고 있다. 혈검, 그 어리석은 사냥개와는 달리 너의 충성심은 굳건하면서도 순수하다는 것을.

“천주시여……!”

- 가거라. 너를 기다리는 곳으로. 그곳에서 네 주인의 또 다른 충복과 힘을 합쳐 새로운 임무를 완수하라. 이제는 진정 대계(大計)의 완성이 머지않았으니.

그 어느 때보다도 선명하게 전해지는 주인의 신뢰에, 대술사는 벅차오르는 감격을 참지 못하고 눈물을 흘렸다.

“목숨을 걸고 제게 주어진 소명을 완수하겠나이다.”

- 믿겠다. 지금껏 늘 그래 왔듯이.

나직한 머릿속 울림과 함께, 대술사의 전신을 휘감고 있던 어둠의 일부가 그녀의 몸속 깊숙이 파고들었다.

아니, 본래 한 몸이었던 것처럼 스며들었다.

스아아아.

몸속 깊숙한 곳에서 솟구치는 미증유(未曾有)의 기운에 대술사는 전율했다.

동시에 주인에게 선물 받은 이 거대하고도 새로운 힘이 지금 이 순간 무엇을 원하는지, 어디로 자신을 이끄는지 느낄 수 있었다.

‘청해(靑海).’

그 순간.

화아아악!

불현듯 부풀어 오른 새하얀 섬광이, 가녀린 전신을 뒤덮으며 터져 나왔다.

팟.

모든 것은 찰나에 벌어졌고, 찰나에 끝났다.

그리고 마침내 대술사가 흔적도 없이 사라진 그 칠흑 같은 공간 속에서, 홀로 남게 된 절대자는 조용히 뇌까렸다.

- 시간이 흐르고 있군.

조금씩 흩어지는 어둠 속, 정체를 알 수 없는 녹광(綠光)이 흐릿하게 빛나고 있었다.
```

## Final English reading copy

```markdown
# Chapter 1054

“Awaken.”

Nothing more was needed.

At the brief whisper that roused her mind as it sank beneath the surface of sleep and took command of her thoughts, her tightly shut eyelids opened without the slightest movement.

“Ah.”

A short gasp, followed by an exhalation.

At last conscious again, the Grand Mage looked at the pitch-black darkness pressing in from every side and finally understood.

Her gamble in the final moment, taken at the risk of her life, had succeeded.

And that was why she, who had suffered a wound severe enough to kill her, was still alive.

“Heaven above and earth below, all demons bow in reverence!”

The Grand Mage poured out the eight characters of the sacred words engraved upon her soul, then hurriedly prostrated herself before the deep darkness.

First she dropped to both knees, then placed both arms on the ground, and finally struck her forehead against the stone hard enough to make it ring.

Thud. Thud. Thud.

Blood drops fell onto the cold stone floor as pain throbbed through her forehead, but the Grand Mage paid them no mind.

It was all thanks to one being’s grace that she could prostrate herself like this—and that she had recovered the arm and leg torn away when she was swept up in unstable space.

“This foolish and lowly servant presents herself before the great Lord of Heaven.”

At the Grand Mage’s voice, filled with utmost reverence, the darkness surrounding her rippled slowly.

“Speak. Everything you saw and heard.”

A short phrase echoed inside her mind.

But the Grand Mage knew better than anyone that her master wasn’t asking about the outcome of the battle.

Her master’s attention was fixed on only one person.

“I sought to carry out the Lord of Heaven’s command, even at the cost of my life.”

The Grand Mage continued, not daring to raise her face.

She told him roughly how many allies had fallen to Jin Taekyung, how many Black Ghosts had been brought down along the way, and how the battle had unfolded from beginning to end.

“So, shameful as it is, I had no choice but to flee in haste. Please, kill me.”

When she had finished speaking, the Grand Mage quietly bit her lip.

She had done her utmost, but not everything had gone perfectly according to plan.

Then, amid the Grand Mage’s fear, her mind echoed once more.

“You did not see the Blood-Sword’s life taken?”

“…No. And I failed to predict that the two Daoists of the Zhongnan Sect and Sima Gong would betray us again. Even if I had ten mouths, I would have no excuse.”

The Black Night King Sima Gong, who had been allied with the Blood-Sword Demon Lord.

And the Roaring Fury Swordsman Song Il and the Taeeul Merciless Sword Hwangbo Eom, whom he had drawn in as well.

The Blood-Sword Demon Lord, who had recruited the traitors starting with the Black Night King, had no idea. Under the original plan, they would all have been dead by now.

And Jin Taekyung should have killed them before the real battle even began.

“However, things went wrong in an unexpected way even before that.”

“What?”

“Kongtong.”

The Kongtong Sect.

They had been the first supporting players in the stage the Grand Mage had planned.

The survivors of the Kongtong Sect, driven from Dunhuang, were supposed to join the allies in the rear and reveal every detail of what they had seen and heard.

The overwhelming military strength of Dark Heaven. The strange power called Magic.

And, finally, the crucial seed of suspicion that would expose the traitors—that had been the Grand Mage’s intention.

“So I let word of the traitors reach their ears. Then I let them go, pretending I had failed to find them.”

She hadn’t merely lost track of them.

She had let them go. Deliberately.

It was an audacious claim, almost unbelievable when spoken of the Kongtong Sect, one of the Nine Sects and One Gang. Yet even now, the Grand Mage was certain.

Had she and the mages under her command joined the pursuit with the intent to kill, the Kongtong Sect would have been wiped out in Dunhuang.

But the Grand Mage had made no effort to capture and kill them.

Unlike the Blood-Sword Demon Lord, her goal hadn’t been victory.

Her only separate order from the Lord of Heaven had been to ensure Jin Taekyung’s survival and growth.

That was why at least some of the Kongtong Sect had survived.

When she heard that their survivors, including the Sect Leader, had shaken off the relentless pursuit and escaped the encirclement, the Grand Mage had smothered a laugh to keep the Blood-Sword Demon Lord from noticing. She had already been thinking of what would come next.

The survivors would return and reveal the truth. Jin Taekyung would execute the handful of traitors and become the enemy’s new rallying point, then win a sweeping victory in battle.

A plan that was both safe and perfect.

But…

“Some of the survivors who knew the truth, including the Kongtong Sect’s Sect Leader, vanished without a trace.”

At that, the darkness rippled violently.

“Vanished without a trace?”

“Yes. I beg forgiveness, but even the power of the sorcery you granted this servant could not find them. At some point, they disappeared to a place I cannot guess.”

The first unexpected crack had appeared, but even the Grand Mage could not follow their trail.

Time passed. The real battle began. New cracks appeared one after another.

The traitors, for some reason, had again chosen the foolish path despite the battle turning against them.

Jin Taekyung had severed his own heart meridian and gambled his life.

And the Grand Mage herself had been put in danger by the arrival of the Fire King and the Bow Saint.

“Please punish this lowly servant, who failed to carry out the mandate of Heaven.”

She had achieved her immediate objective, but that was all.

The Grand Mage bowed her head even lower.

She waited for her master’s fury to shake heaven and earth.

But contrary to her fears, the mind-voice that echoed from deep within her a moment later, as if resonating, was as emotionless as ever.

“Raise your head.”

The Grand Mage obeyed as if entranced. Beyond the dense veil covering her face, the darkness writhed as though alive.

It was deeper and denser than at any point in the past several decades.

“Can you see it? Can you feel it?”

The Grand Mage didn’t answer her master’s question.

No—she couldn’t answer.

Her pupils, which had rolled back until their whites showed at the sight of the darkness, were already turning black.

“I can see. I can feel. Everything hidden inside you. Clearly.”

*Whoooosh.*

The darkness that had completely consumed her retinas didn’t stop there. It continued to spread.

Faster. Deeper.

It seized the mind of its loyal servant, whose slender frame trembled as she lost her reason. It swept through her thoughts and shook her soul, then returned to its master.

As if nothing had happened.

*Thump.*

“Ah—h-hah. Hah!”

The moment the darkness left her eyes and their focus returned, the Grand Mage crumpled like a marionette with its strings cut, gasping for breath.

“M-My Lord of Heaven.”

Her voice trembled. Her eyes were full of fear.

The Grand Mage knew instinctively.

Just now, the Lord of Heaven had read and looked into every one of her thoughts and memories.

At the same time, an awe so intense it raised goose bumps drove out her fleeting fear and enveloped her whole body.

*That power…*

Remembering the force that had seeped into her body and seized her soul, the Grand Mage trembled.

She knew it had been no more than a tiny fragment of his power. That only made her wonder and shock all the greater.

*Just how far do his powers reach?*

Even a thousand-year-old tree could never touch the clouds.

But the Lord of Heaven was different.

From the moment she had first met him, he had been the absolute ruler, beyond compare. And day by day, he had grown stronger to a degree that made the very word *limit* meaningless.

So much so that even the Grand Mage, one of his closest confidants, was astonished.

And she already had an idea where this unbelievable change had begun.

*Jin Taekyung. No—the Chosen One.*

There could be no doubt.

A little more than two years ago, when bloodshed swept through Shanxi Province and the epithet Hidden Dragon became known throughout the land, her master had begun to change as well.

He had begun waking more often from deep slumbers that could last up to ten years and, even at their shortest, nearly a year. Each time, the Grand Mage could feel the Lord of Heaven’s power had grown stronger.

Even here, today.

*But what could that possibly have to do with—?*

The question came naturally.

But the next moment, a thunderous echo shook her mind, turning her thoughts blank.

“No question belongs to you.”

“……!”

“Do not forget what your master wants. Do not forget what you must do.”

The Lord of Heaven’s voice seemed to pierce her soul. The Grand Mage realized she had momentarily forgotten something.

That the being before her was an absolute ruler, transcending everything.

That, as his servant, she could not permit herself to question or doubt him.

“Please, please kill this irreverent servant!”

The Grand Mage cried out as if she were coughing up blood.

Prostrate, as though she would become one with the cold stone floor, she reaffirmed her loyalty—a devotion that could only be called fanatical—and praised her master.

She kept at it until her clear, calm voice, like the sound of a silver bell, grew hoarse and cracked.

Until her master finally issued his command to the lowly servant who had dared, even for an instant, to harbor a question.

“That is enough.”

*Rustle.*

The darkness rippled gently for an instant and wrapped around the Grand Mage.

As if caressing her tenderly.

“Nothing of the sort will ever happen. Your master knows that, unlike the foolish hound called the Blood-Sword, your loyalty is steadfast and pure.”

“My Lord of Heaven…!”

“Go. To the place waiting for you. Join forces there with another of your master’s loyal servants and complete a new mission. The completion of the great plan is now truly close.”

At the trust in her master’s words, conveyed more clearly than ever before, the Grand Mage couldn’t hold back her overwhelming emotion. Tears filled her eyes.

“I will risk my life to fulfill the mission entrusted to me.”

“I believe you. Just as I always have.”

As his quiet voice echoed in her mind, some of the darkness wrapped around the Grand Mage sank deep into her body.

No—it seeped into her as if they had always been one.

*Fwoosh.*

The Grand Mage shuddered as an unprecedented power surged from deep within her.

At the same time, she could sense what this immense new power her master had given her wanted at that very moment, and where it was leading her.

*Qinghai.*

At that instant—

*Whoooom!*

A brilliant white flash suddenly swelled and burst out, engulfing her slender body.

*Pop.*

It all happened in an instant, and ended in an instant.

At last, the Grand Mage had vanished without a trace. In the pitch-black space where she had disappeared, the absolute ruler remained alone and murmured quietly.

“Time is passing.”

As the darkness slowly dispersed, a mysterious green light glimmered faintly.
```
