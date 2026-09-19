<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0498.txt",
      "sha256": "c13422e695cb1f1f8ad017e6c8a2ebf1dca7718e35cd19078f800a09b578b867",
      "bytes": 12752
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7034bfcd5a24b5a68d34c853282ed481477e035d668e2d933b62892c21033a1e",
      "bytes": 5198
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "445d39167e55f207979117cefb25eb9826901650c1a4482225cf4ebaee2ec8fc",
      "bytes": 158326
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d0142e90d5f8f025c7cf85de44abffb461432525dbda9f6113d4b4e75df8ad58",
      "bytes": 553
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "5d11a808620aa04e1ea3c36b7bb03393a867cc17012c925c8d2ad0b8cf7f74e3",
      "bytes": 686
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "8457df0b16bba3b28071a9b8f3b017e5d3cb9f223399a144f28999d908c31939",
      "bytes": 1108
    },
    {
      "path": "characters/Jang Taebo.md",
      "sha256": "69fb768b4ffcd91d18635f6a53d5dbba8fe3aadbf427366d690cfcc668002170",
      "bytes": 1259
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "6c96924d86ce87e0f1f047255c641ec354658fa3d20286fa03940201ec380394",
      "bytes": 1239
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "0cf4129410c15857c049fd165ac8d37c33bf722d33eeab46eb419f190020612b",
      "bytes": 916
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "a453309a4b29c5a50f9634ef45adc66d999810beccbd64c1fb7ff7e0f1acf472",
      "bytes": 954
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fcd89ef22d5cd9bc5646cb7dfc2a01c58c5dc8bb04ac6b55736f44af7216f5ad",
      "bytes": 153645
    }
  ],
  "estimated_tokens": 12116
}
-->

# Durable State Update — Chapter 498

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 498. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 498. Profile updates may replace only one
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
  "chapter": 498,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 498,
    "continuity_sources": [498],
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
    "Taekyung suspects Dark Heaven's regeneration, teleportation, and Moving Formation are manifestations of Magic connected to the Gate.",
    "Taekyung told Jeok that he came from another world, that an evil force from it is linked to Dark Heaven, that the corrupted imugi was their work, and that a fully opened Gate could release monsters.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people; the severely injured Dongting Fisherman may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense.",
    "Jeok's innate qi is damaged and steadily diminishing despite the Thousand-Year Snow Ginseng and the Divine Physician's treatment; Taekyung remains uncertain whether Jeok recovered without lasting aftereffects.",
    "Mungyeong is the Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; before becoming the Slaughter Saint, he was called Killing Ghost, and he saved countless people as the Divine Physician. He once belonged to the vanished assassin sect Salcheonmun and taught several assassins there, none of whom are believed alive.",
    "Mungyeong recognizes Taekyung's Heavenly Martial Physique as innate and distinct from Cheongpung's more refined physique.",
    "After seven days and nights of poisoned tests, Taekyung evaded Mungyeong's blinding final sword stroke and demonstrated the basics Mungyeong sought; Mungyeong intends to teach him secret martial arts without a formal Master-Disciple relationship.",
    "Taekyung detoxified Potent Seven-Step Soul-Chasing Powder, but Sinews and Meridians damage permanently reduced Strength and Agility by 5 each; he has stored the Water God Dragon's dismantled materials and Origin Essence in his inventory."
  ],
  "continuity_sources": [
    497,
    496
  ],
  "open_questions": [
    "Will Zhuge Feng's formation permanently seal the Gate gap, and what lies beyond it if the Gate is reopened?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "Has Jeok fully recovered from the Formless Ultimate Poison, and will Taekyung use the Water God Dragon's Origin Essence to aid him?"
  ],
  "safe_through": 497,
  "temporary_decisions": [
    "Render 산공독 as Energy-Dispersing Poison, 강력한 산공독 as Potent Energy-Dispersing Poison, 칠보추혼산 as Seven-Step Soul-Chasing Powder, 강력한 칠보추혼산 as Potent Seven-Step Soul-Chasing Powder, 심각한 복통 as Severe Stomachache, 고기 방패 as Meat Shield, 독 장아찌 as Poisoned Pickle, and 독의 as Poison Physician; retain secret martial arts, Master-Disciple relationship, Killing Ghost, and Fake Murim Martial Artist, and preserve 악 as Agh in the Quest interface; render 실명산 as Blindness Powder, 살천문 as Salcheonmun, and 스승의 날 as Teacher’s Day.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 혈어 as Blood Fish, and 변이된 송사리 as Mutated Minnow; render 강력한 마비산 as Potent Paralysis Powder, 강력한 미혼산 as Potent Soul-Bewitching Powder, 전신 마비 as Full-Body Paralysis, 독성 흡수 as Poison Absorption, and 해독 as Detoxification.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter; render 해시 as hour of the Pig, 한 식경 as half an hour, 타구봉 as Dog-Beating Staff, 창룡 as Azure Dragon, and 무량수불 as Infinite Life Buddha; preserve geun as the traditional weight unit with a footnote.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, and 천기 as heavenly patterns.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 강강수월래 as Ganggangsullae, 생사부 as Book of Life and Death, 기막 as qi curtain, 무극태을검 as Martial Extremity Grand Unity Sword, 이룡 as Two Dragons, 원정 as Origin Essence, 내단 as inner core, 영험한 기운 as sacred energy, 대호 as great tiger, and 취팔선권 as Drunken Eight Immortals Fist."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 살성     | **Slaughter Saint**           | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 진룡대    | **Jin Dragon Squad**             |
| 항산검문   | **Mount Heng Sword Sect**        |
| 열화문    | **Fire Gate Clan**               |
| 무당파    | **Wudang**                       |
| 제갈세가   | **Zhuge Clan**                   |
| 삼류     | **Third Rate**    |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 영약     | **elixir**                                       |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기루     | **pleasure house**                               |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장문인    | **Sect Leader**                              |
| 대주     | **Squad Leader** / **Commander**             |
| 부대주    | **Vice Squad Leader** / **Deputy Commander** |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 장태보 | **Jang Taebo** | Former Guild Leader of the Ironcraft Guild; now lives near Jeongyang and is sought as a Master Artisan. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대태원진가 | **great Jin Family of Taiyuan** | Formal exalted reference to the Jin Family of Taiyuan. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 철기방 | **Ironcraft Guild** | Hubei guild composed mainly of skilled craftsmen and closely associated with the Nine Sects and One Gang. |
| 철기방주 | **Guild Leader of the Ironcraft Guild** | Title of the Ironcraft Guild’s leader; the current leader is Jang Taebo’s disciple. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 개방도 | **Beggars' Sect disciple** | Member of the Beggars' Sect. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 칠보추혼산 | **Seven-Step Soul-Chasing Powder** | Named extreme poison used in Mungyeong's training test. |
| 실명산 | **Blindness Powder** | Poison powder that temporarily blinds Taekyung. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 장태보 | 혁무진 | elder_smith_to_young_martial_artist | you / wet-behind-the-ears brat | gruff and insulting | Insults Mujin after Mujin whispers that Jang is senile. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 위팽 | 혁무진 | mentor_to_junior_martial_artist | Hyuk Mujin | blunt and testing | Wipeng addresses Mujin by name when beginning to assess and train him. |
| 혁무진 | 위팽 | junior_martial_artist_to_mentor | Great Hero Wipeng | formal-deferential | Mujin uses 위팽 대협 when reacting to Wipeng's recognition and instruction. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 진위경 | martial_companion_to_family_head | Great Hero Jin | familiar and polite | Asks Jin Wikyung not to exclude the Beggars' Sect from the defense. |
| 문경 | 혁무진 | traveling_companion_to_traveling_companion | Martial Warrior Hyuk | formal-polite | Mungyeong asks Mujin to deliver water to Taekyung and lets Mujin receive the credit. |
| 혁무진 | 문경 | traveling_companion_to_traveling_companion | Mungyeong | casual-familiar | Mujin recognizes Mungyeong while reacting to Taekyung's dismantling work. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 497
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 496
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 496
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jang Taebo.md

# Jang Taebo (장태보)

- **Safe through:** Chapter 347
- **Aliases:** None
- **Role:** Former Guild Leader of the Ironcraft Guild and one of the world’s renowned smiths; spent a full jiazi working at the forge before retiring and living anonymously for more than ten years in a village near Jeongyang; after seeing Taekyung’s enormous supply of Ten-Thousand-Year Cold Iron, he accepts the commission to forge it into a weapon capable of making the world tremble and waives monetary payment because the opportunity is sufficient; fifteen days before Chapter 243, he handed Hyuk Mujin the resulting spear for delivery to Taekyung; Jeok Cheongang’s Flame Divine Palm destroyed his home, and he asks Taekyung to have it rebuilt.
- **Personality:** Blunt, cantankerous, solitary, and proud; values an untroubled retirement and protects his anonymity, while quietly caring for the neighboring boy Hanga.
- **Voice:** Curt, gruff, and dryly teasing; rejects requests with flat finality.
- **Relationships:** His disciple is the current Guild Leader of the Ironcraft Guild; neighboring boy Hanga is his only conversational partner, and Jang Taebo gives him candy while pretending annoyance.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 495
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 497
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history who passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance who asked him to look after and instruct Jin Taekyung, and Mungyeong has completed his poisoned tests of Taekyung’s basics without a formal Master-Disciple relationship and intends to teach him secret martial arts.

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 318
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and Commander of the Jin Dragon Squad; one of the Jin Family’s three Peak masters
- **Personality:** Loyal, observant, teasing, capable, and resigned to Jin Wikyung’s impulsive behavior. Respects the dead and urges others to live on their behalf.
- **Voice:** Weary and knowing, with dry humor when addressing Jin Wikyung or Jin Taekyung. Uses Sound Transmission when appropriate.
- **Relationships:** Trusted guard and retainer of Jin Wikyung; a reliable senior ally of Jin Taekyung. He has fought beside the Jin Family in major battles, including the conflict with Mount Heng, and remains alert to threats connected with Dark Heaven. The Human Butcher has claimed him as a personal target in a planned attack.

## Korean source

```text
＃498화



길었던 잠에서 깨어 정신을 차린 순간, 문득 뇌리를 스치는 생각이 있었다.

‘설마 아직도 해독이 안 됐나?’

온통 까맣게 물든 시야.

하지만 일말의 불안감은 곧장 사그라들었다. 먹빛 하늘 위로 희미한 빛을 뿌리는 달을 확인한 나는 잠긴 목소리로 중얼거렸다.

“시바, 좀 깨워 주고 가든가.”

실명산 때문인 줄 알았는데, 그냥 날이 어두워진 것뿐이었다.

보아하니 정신을 잃은 사이에 상당한 시간이 흐른 모양이었다. 대자로 뻗은 채 멍하니 하늘만 올려다보던 나는 부스스 몸을 일으켰다.

‘도대체 어떻게 된 거지?’

워낙 무의식중에 움직이기도 했고, 실명산에 중독된 채로 기절했기 때문에 당시의 상황을 보진 못했다. 나는 흙투성이인 몸 이곳저곳을 만져 보았다.

‘따로 다친 곳이 없는 걸 보면 분명히 막은 것 같긴 한데.’

결과는 짐작할 수 있지만 과정이 쉽게 그려지지 않는다. 내가 어떻게 움직였더라? 곰곰이 그때의 감각을 떠올리려 해 봐도 온통 안개처럼 희끄무레했다.

대신, 한 가지 사실은 알 수 있었다.

띠링.



- 임무 : [문경]에게 인정받기 (완료)

- 돌발 퀘스트, [가짜 무림인]을 성공적으로 완료했습니다!

- 퀘스트 완료 보상이 지급됩니다!

- 상당량의 경험치를 획득했습니다!

- 10포인트를 획득했습니다!

- 뛰어난 업적, [맹독 소믈리에]를 달성했습니다!

- 당신은 특별 제조된 십여 종류 이상의 맹독을 맛보고 해독했습니다. 당신의 튼튼한 몸뚱어리와 해독 능력에 경의를 표합니다!

- [독 저항력]이 크게 상승합니다!

- 놀라운 업적, [와, 이걸 사네]를 달성했습니다!

- 당신은 생사의 기로에서 새로운 깨달음의 실마리를 잡았습니다!

- [기감]이 보다 날카로워집니다. 수련을 통해 더욱 높은 경지로 나아가십시오!

- 연계 퀘스트, [가짜 무림인-2단계]가 생성되었습니다!

- 연계 퀘스트의 임무는 [문경]의 향후 방침에 따라 결정됩니다!

- 악!



“…….”

악 같은 소리 하고 자빠졌네. 동정호가 아니라 요단강을 건널 뻔한 나로서는 치가 떨릴 지경이었다.

‘연계 퀘스트라니.’

어느 정도 예상한 일이라 해도 걱정이 되는 건 어쩔 수 없다. 1단계에서 눈 감고 살성의 일검을 피하라는데, 2단계에서는 도대체 무슨 개 같은 짓거리를 준비해 놨을까. 그나마 보상이 짭짤하다는 것이 한 줄기 위안이다.

‘그래도 이 정도면 몸으로 때운 보람은 있는 건가.’

비록 레벨 업은 못 했지만 상당량의 경험치를 얻었고, 칠보추혼산에 중독되며 잃었던 포인트도 복구했다.

그리고…….

‘업적 달성 제목 어떤 새끼가 지었냐.’

[맹독 소믈리에]와 [와, 이걸 사네].

이번에 달성한 이 두 가지 업적은 심히 불쾌한 제목과는 별개로 제법 괜찮은 수확이라고 할 수 있었다.

전자를 통해 얻은 독 저항력은 말할 것도 없이 땡큐고, 후자는 지금 당장은 조금 애매해 보일지 몰라도 큰 선물이다.

‘깨달음의 실마리.’

근래 들어 벽을 느끼고 있던 내게는 다른 무엇보다 반가운 소식이다. 물론 열화문의 초절정 무공에, 분기별로 영약까지 든든하게 처먹으며 초고속으로 성장한 내가 이런 말을 하면 무림 공적 취급받기 딱 좋겠지만.

‘그래도 막힌 건 막힌 거니까.’

이류, 삼류의 경지에 머무르는 무림인에게 무엇이 필요한지 묻는다면, 십중팔구는 무공 비급과 영약이라 말한다. 그러나 절정 혹은 그 이상의 경지에 도달한 고수들의 대답은 다르다.

‘깨달음.’

십 년, 이십 년. 혹은 그 이상의 세월을 기다려도 쉽게 찾아오지 않는 것이 바로 깨달음이다. 아무리 뛰어난 무공을 익히고 영약을 섭취한다고 해도 올라갈 수 있는 경지에는 한계가 있다.

영약 처먹는다고 초절정 고수 되고, 반로환동하면 누가 피땀 흘려 수련을 하겠나. 분명한 한계로 인해 벽을 넘지 못하니까 그저 죽어라 수련에 매달리는 거다.

일전에 궁기방에게 들은 바에 의하면, 심상(心想)의 영역을 넓혀 깨달음을 얻겠답시고 아편을 복용하는 무림인들도 적지 않다고 했다.

왜 그딴 걸 하냐고 묻자, 돌아온 대답은 간단했다.



‘그 작자들도 알아. 이대로라면 아편에 중독되리라는 걸.’

‘아는 놈들이 왜 그래?’

‘무림인이니까.’



짧지만 모든 것을 설명하는 한마디.

무림인은 그런 생물이다. 더 강해질 수만 있다면 무슨 짓이든지 할 수 있는 종자들. 아편이라는 마약보다 무공에 취했고, 힘에 중독되어 버렸다. 그리고 그건 나 역시 크게 다르지 않다.

‘더, 더 강해지고 싶다.’

과거에는 상상할 수도 없었을 만큼 많은 것을 갖게 된 지금도 마찬가지다. 다만 여타의 무림인과 결정적인 차이가 있다면, 나는 무언가를 얻고자가 아닌 지키기 위해 강해지려 한다는 점이다.

‘현재에 만족했다면 문경의 수련을 받아들이지도 않았겠지.’

그런 의미에서 깨달음의 실마리를 얻었다는 건 엄청난 성과다.

단 한 가지 사소한 문제가 있다면…….

‘의사 선생님, 아무것도 기억나지 않습니다.’

내가 정확히 뭘 했는지조차 모른다는 거다. 개 같은 거.

아니, 진짜 어떻게 한 거지? 아슬아슬하게 피한 것 같긴 한데, 그 후를 모르겠다.

‘수련을 계속하다 보면 알 수 있으려나.’

당시의 감각을 떠올리려고 노력해 봤지만 당장은 안개를 헤매는 것처럼 허망하기만 하다. 한숨을 푹 내쉬며 자리에서 일어나 옷에 묻은 흙을 털고 있던 그때였다.

쉬이익, 펑!

저 멀리, 검게 물든 하늘 위로 솟구친 한 줄기 푸른 불꽃이 화려하게 폭발했다.

‘신호용 폭죽?’

무슨 일인가 싶어 수련 장소를 빠르게 벗어나자, 경계를 서고 있던 무인들을 만날 수 있었다.

“무슨 일입니까?”

“아, 진 대협. 이제야 나오셨군요.”

누덕누덕 기운 옷차림에 허리에 매달린 두 개의 매듭. 호북 분타에 소속되어 있는 것이 분명한 개방도가 어깨를 으쓱하며 말을 이었다.

“색이 푸른 걸 보니 방문객입니다. 미리 들어서 알고 있긴 했는데, 생각보다 늦었군요.”

“방문객?”

아니, 여기가 무슨 관광 명소도 아니고.

워낙 기밀로 취급하다 보니 찾아올 만한 사람이라고 해 봐야 선뜻 떠오르는 곳이 없었다. 기껏해야 이곳에 모인 세 문파, 그리고 관부 정도인데. 인력 충원이라면 굳이 방문객이라고 표현할 리는 없고.

“어디에서 온 건데요? 제갈세가? 아니면 무당파? 아, 거기 장문인께서 드디어 오신 건가.”

“예?”

개방도를 비롯한 무인들이 별 희한한 놈 다 보겠다는 표정으로 나를 바라보았다.

“어, 음. 못 들으셨습니까?”

“뭘요?”

“지금 오고 있는 방문객 말입니다.”

“그게 무슨……. 혹시 제가 아는 사람들이에요?”

내 물음에 고개를 끄덕인 개방도가 대답했다.

“예. 태원진가니까요.”

“……어?”

어디라고?



* * *



철벅! 처처척!

절도 있는 발걸음이 하늘 위의 달을 비추는 강물을 밟고, 모래 위로 새로운 발자국들을 찍어 나간다.

마치 한 몸처럼 움직인 오십여 명의 무인들이 좌우로 도열하자, 그 사이로 천천히 걸음을 옮긴 한 사람이 나를 발견하고 멈춰 섰다.

“오랜만입니다.”

여전히 날카로운 눈매와 더욱 늘어난 흉터. 나는 일 년 만에 마주한 낯익은 얼굴을 향해 피식 웃어 보였다.

“얼굴이 더 살벌해지셨네. 이 정도면 귀검(鬼劍)이 아니라 귀면(鬼面)이라고 해도 되겠어요.”

“손봐야 할 놈들이 한둘이 아니라서 말입니다. 본가의 발이 넓어지니 별의별 놈들이 꼬이더군요.”

“누군지 말만 하세요. 제가 손봐 주게.”

“그럴 필요 없습니다. 이미 손쓸 수도 없는 곳으로 떠났으니. 그리고…….”

가늘게 뜬 눈에는 웃음이, 이어지는 목소리에는 감회와 기쁨이 묻어 나왔다.

“고작 소, 돼지를 잡는 일에 신룡(神龍)이 나설 필요는 없습니다.”

귀검 위팽. 진위경의 오른팔이자 한때 내 참교육 담당이었던 그가 나를 향해 깊이 포권을 취했다.

“대태원진가 진룡대주 위팽. 삼공자님을 뵙습니다.”

“삼공자님을 뵙습니다!”

거대한 외침이 깊은 밤의 적막을 터트리며 울려 퍼졌다. 좌우로 철탑처럼 늘어선 무인들의 전신으로부터 힘찬 기운이 느껴진다. 하나같이 가슴에 수실로 새겨 넣은 진룡(進龍)이라는 두 글자처럼.

‘이야, 태원진가 언제 이렇게 컸냐.’

항산검문과의 전쟁에서 턱없이 부족한 일류 고수의 숫자 때문에 머리 맞대고 좆 됐다를 중얼거리던 게 엊그제 같은데, 당장 이 자리에 모인 진룡대의 무인들만 봐도 최소가 일류 고수다.

‘보고만 있어도 뽕 찬다. 뽕이 차.’

가주의 장기 부재, 극심한 인력난, 집보다 기루를 더 좋아하는 삼공자와 기타 등등의 문제로 천천히 몰락해 가던 태원진가가 떡상한 것을 보니 절로 가슴이 벅차 온다.

‘이 맛에 가문 키우는 건가.’

그저 흐뭇하게 위팽과 진룡대를 바라보던 바로 그 순간, 위팽의 등 뒤로 산통 깨는 목소리가 들려왔다.

“어이 씨, 깜짝이야. 밤중에 왜 이렇게들 소리를 지르고 그러시오? 나처럼 심장 약한 늙은이가 놀라서 급사라도 하면 어쩌려고.”

아마 그럴 일은 없어 보이는데.

노인이라고는 믿기지 않을 만큼 우람한 근육을 지닌 그를 유심히 바라보던 나는, 마침내 옛 기억을 끄집어내는 데 성공했다.

“절대 태보해?”

전(前) 철기방주. 장태보의 표정이 와락 일그러졌다.

“저저, 말하는 싸가지 보게. 내가 네놈 친구냐!”

일 년이라는 짧은 시간 동안 엄청난 위상을 쌓아 올린 나지만, 노빠꾸 장인인 장태보에게는 아무런 상관도 없어 보였다.

나 역시 그 때문인지는 몰라도 더 정이 가고 반가웠다. 게다가 그가 혼신의 힘을 다해 만들어 준 백염(白炎) 덕분에 여러 번 목숨을 건지기도 했으니까.

“아니, 어르신이 여기 웬일이십니까?”

내 물음에 대한 대답은 장태보의 입이 아닌, 다른 곳에서 들려왔다.

“내가 특별히 청하여 모셨다.”

태원진가의 도착 소식을 듣고 급히 모여든 사람들이 웅성거리며 좌우로 갈라졌다. 인의 장막을 가로지르며 다가오는 한 사람의 모습에, 조금 전보다 더욱 큰 외침이 울려 퍼졌다.

“대태원진가 진룡대주 위팽. 주군께 인사 올립니다.”

“충(忠)!”

“그만.”

다른 때였다면 위팽 손부터 붙잡고 왈츠를 췄겠지만 지금은 수많은 시선들이 지켜보고 있었다. 진중하면서도 위엄 있는 표정으로 손을 내저은 진위경이 묵직한 중저음으로 말을 이었다.

“진룡대주. 그리고 장 노야. 오느라 고생 많았네.”

“아닙니다. 주군.”

“이 늙은이는 신경 쓰실 것 없습니다. 소가주.”

위팽이야 두말할 필요조차 없는 심복이고, 나한테는 이놈 저놈 하는 장태보도 진위경에게만큼은 깍듯하게 예의를 차린다. 이미 한참 전에 은퇴했다더니, 못 본 사이 태원진가에서 하청이라도 받고 있나?

내 의문을 뒤로하고 진위경이 재차 입을 열었다.

“오는 길이 고단했을 터, 우선 다 같이 자리를 옮깁시다.”

저 ‘다 같이’에 내가 포함되어 있음은 어렵지 않게 알 수 있었다. 그리고 저기에서 헐레벌떡 달려오는 놈은 포함되지 않았다는 사실도.

“진룡대 부대주 혁무진! 지금 막 경계를 마치고 복귀했습니다!”

“…….”

경계 같은 소리 하고 있네.

거짓말을 칠 거면 눈곱부터 떼고 와, 이 자식아.
```

## Final English reading copy

```markdown
# Chapter 498

The moment I woke from my long sleep and came to my senses, a thought suddenly flashed through my mind.

*Could I still be poisoned?*

My entire field of vision was pitch-black.

But the faint anxiety quickly faded. After confirming the moon casting a dim light across the ink-black sky, I muttered in a hoarse voice.

“Shit, you could’ve woken me before leaving.”

I had thought it was because of the Blindness Powder, but it was simply dark outside.

A considerable amount of time seemed to have passed while I was unconscious. I had been sprawled out on my back, staring blankly at the sky, before slowly pushing myself upright.

*What the hell happened?*

I had moved almost entirely unconsciously, and since I’d passed out while poisoned by the Blindness Powder, I hadn’t seen what happened at the time. I felt my dirt-covered body all over.

*I must have blocked it somehow. Otherwise, I’d have more injuries.*

I could guess the result, but the process was difficult to imagine. How had I moved? Even when I desperately tried to recall the sensations from that moment, everything remained hazy, like a fog.

Instead, I learned one thing for certain.

Beep.

> **System**
>
> - Mission: Earn Mungyeong’s Recognition (Complete)
>
> - The Sudden Quest, Fake Murim Martial Artist, has been successfully completed!
>
> - The Quest completion Reward has been issued!
>
> - You have gained a considerable amount of EXP!
>
> - You have gained 10 points!
>
> - You have achieved the Outstanding Achievement, Deadly Poison Sommelier!
>
> - You have tasted and detoxified more than ten types of specially manufactured deadly poison. We salute your sturdy body and Detoxification ability!
>
> - Poison Resistance increases significantly!
>
> - You have achieved the Amazing Achievement, Wow, You Survived That!
>
> - At the crossroads between life and death, you grasped a clue to a new enlightenment!
>
> - Qi Sense becomes sharper. Train to advance to an even higher realm!
>
> - The Follow-up Quest, Fake Murim Martial Artist—Stage 2, has been created!
>
> - The objective of the Follow-up Quest will be determined by Mungyeong’s future plans!
>
> - Agh!

“……”

*Like hell.*

As someone who had nearly crossed the Jordan River instead of Dongting Lake, I was furious.

*A Follow-up Quest.*

Even if I had expected something like this, I couldn’t help feeling worried. In Stage 1, I had been told to evade the Slaughter Saint’s sword stroke with my eyes closed. What kind of insane bullshit had they prepared for Stage 2?

The only consolation was that the rewards were pretty generous.

*At least putting my body through hell had been worth something.*

Although I hadn’t leveled up, I had gained a considerable amount of EXP and recovered the points I had lost after being poisoned by Seven-Step Soul-Chasing Powder.

And…

*Which asshole came up with those Achievement titles?*

Deadly Poison Sommelier and Wow, You Survived That.

Despite their deeply unpleasant names, the two Achievements I had earned this time were actually quite valuable.

The Poison Resistance I had gained from the first one was obviously appreciated. The second one might seem a little vague for now, but it was a tremendous gift.

*A clue to enlightenment.*

For someone like me, who had recently begun to feel a wall in front of him, there was no more welcome news.

Of course, if I said that after growing at breakneck speed by learning the Fire Gate Clan’s Supreme Peak martial arts and stuffing my face with elixirs every quarter, I’d be liable to be treated as an enemy of the Murim.

*But a wall is still a wall.*

If you asked a martial artist stuck in the Second Rate or Third Rate realms what they needed, nine out of ten would say martial arts manuals and elixirs.

But the answer given by masters who had reached the Peak realm or higher was different.

*Enlightenment.*

Ten years. Twenty years. Even if they waited longer than that, enlightenment was something that did not come easily.

No matter how outstanding the martial arts they learned or how many elixirs they consumed, there was a limit to how far they could advance.

If stuffing yourself with elixirs could make you a Supreme Peak master and return you to youth, who would bother shedding blood and sweat in training?

They couldn’t overcome the wall because of their clear limitations, so they simply devoted themselves to training as though their lives depended on it.

According to what Gung Gibang had once told me, quite a few martial artists even took opium in an attempt to broaden the realm of their minds and gain enlightenment.

When I asked why anyone would do something so stupid, the answer I got was simple.

*They know, too. They know they’ll become addicted to opium if they keep going like this.*

*Then why do they do it?*

*Because they’re martial artists.*

It was a short answer, but it explained everything.

Martial artists were creatures like that. They were the sort of people who would do anything if it meant becoming stronger. They were more intoxicated by martial arts than by opium, and they had become addicted to power.

And I wasn’t all that different.

*I want to become stronger. Stronger still.*

Even now, when I possessed more than I ever could have imagined in the past, I felt the same way.

There was one decisive difference between me and other martial artists, though.

I wasn’t trying to become stronger so I could obtain something. I wanted to become stronger so I could protect something.

*If I were satisfied with the present, I never would have accepted Mungyeong’s training.*

In that sense, obtaining a clue to enlightenment was an enormous achievement.

There was only one small problem…

*Doctor, I don’t remember anything.*

I didn’t even know exactly what I had done.

Damn it.

No, seriously. How had I done it? I seemed to have barely dodged the attack, but I had no idea what happened afterward.

*Maybe I’ll understand if I keep training.*

I tried to recall the sensations from that moment, but for now, it was only as futile as wandering through a fog.

I let out a long sigh and stood up, brushing the dirt from my clothes.

That was when it happened.

Ssshhk—boom!

Far away, a streak of blue flame shot up into the darkened sky and exploded spectacularly.

*A signal firework?*

Wondering what was going on, I quickly left the training area and encountered the martial artists standing guard.

“What’s going on?”

“Oh, Great Hero Jin. You’re finally out.”

The Beggars’ Sect disciple, clearly belonging to the Hubei branch from his ragged, patched clothes and the two knots hanging from his waist, shrugged and continued.

“Judging by the blue color, it’s a visitor. We’d already heard they were coming, but they’re later than expected.”

“A visitor?”

This wasn’t exactly a tourist attraction.

Since the place was being treated as highly classified, I couldn’t immediately think of anyone who might come here. At most, there were the three sects gathered here and the authorities.

If it were reinforcements, there would be no reason to call them visitors.

“Where are they from? The Zhuge Clan? Or Wudang? Ah, did their Sect Leader finally come?”

“Excuse me?”

The Beggars’ Sect disciple and the other martial artists stared at me as if they had never seen such a strange person before.

“Uh, well. You haven’t heard?”

“Heard what?”

“About the visitor who’s on the way.”

“What does that mean…? Are they people I know?”

The Beggars’ Sect disciple nodded at my question.

“Yes. They’re from the Jin Family of Taiyuan.”

“……Huh?”

From where?

* * *

Splash! Splash-splash!

Disciplined footsteps crossed the moonlit river and left fresh tracks in the sand.

When more than fifty martial artists moved as one and formed lines on either side, a man walking slowly between them spotted me and came to a stop.

“It’s been a long time.”

His eyes were just as sharp as ever, and he had even more scars than before.

I let out a quiet laugh at the familiar face I was seeing for the first time in a year.

“Your face has gotten even more intimidating. At this point, shouldn’t you be called Ghost Face instead of Ghost Sword?”

“There were more than a few bastards who needed dealing with. As our family’s reach has expanded, all sorts of people have crawled out of the woodwork.”

“Just tell me who they are. I’ll take care of them.”

“There’s no need. They’ve already left for a place beyond anyone’s reach. And…”

His narrowed eyes held laughter, while his next words were filled with emotion and joy.

“There’s no need for the Divine Dragon to deal with mere cows and pigs.”

Ghost Sword Wipeng—the right-hand man of Jin Wikyung and the man who had once been assigned to straighten me out—performed a deep martial salute toward me.

“Wipeng, Commander of the Jin Dragon Squad of the great Jin Family of Taiyuan, greets the Third Young Master.”

“Greetings, Third Young Master!”

The tremendous shout shattered the silence of the deep night.

Powerful energy radiated from the bodies of the martial artists standing in lines like iron towers on either side. They were just like the two characters embroidered across every one of their chests: Jin Dragon.

*Wow. When did the Jin Family of Taiyuan get this big?*

It felt like only yesterday that we had been putting our heads together and muttering that we were fucked because we had nowhere near enough First Rate masters for the war against the Mount Heng Sword Sect.

Yet just looking at the Jin Dragon Squad gathered here, the weakest among them was at least a First Rate master.

*I feel high just looking at them. So high.*

The Jin Family of Taiyuan had been slowly declining due to the Family Head’s long absence, a severe shortage of personnel, and a Third Young Master who preferred pleasure houses to his own home, among other problems.

Seeing it rise so dramatically made my chest swell with pride.

*Is this why people build families?*

I was gazing contentedly at Wipeng and the Jin Dragon Squad when a voice from behind him ruined the mood.

“Hey, damn it! You startled me. Why are you all shouting in the middle of the night? What would you do if an old man with a weak heart like me got frightened and dropped dead?”

That didn’t seem very likely.

As I studied the man’s powerful muscles, which were impossible to believe belonged to an old man, I finally succeeded in dredging up an old memory.

“Always do Taebo?”[^1]

[^1]: A Korean internet catchphrase urging people to do Tae Bo; here it puns on Jang Taebo’s name.

The expression of Jang Taebo, former Guild Leader of the Ironcraft Guild, twisted in outrage.

“Look at the manners on this guy. Am I your friend?”

Although I had built up an incredible reputation in the short span of a year, it seemed to mean nothing to Jang Taebo, a master craftsman who never hit the brakes.

Maybe because of that, I felt even more fond of him and happier to see him.

Besides, the White Flame he had forged with everything he had put into it had saved my life several times.

“Elder, what brings you here?”

The answer to my question came from somewhere other than Jang Taebo’s mouth.

“I specifically asked him to come.”

The people who had hurried over after hearing that the Jin Family of Taiyuan had arrived murmured among themselves and parted to either side.

As a man approached through the human curtain, an even louder cry rang out than before.

“Wipeng, Commander of the Jin Dragon Squad of the great Jin Family of Taiyuan, pays his respects to his lord.”

“Loyalty!”

“That’s enough.”

Under different circumstances, I would have grabbed Wipeng’s hand and danced a waltz with him, but countless eyes were watching us.

Jin Wikyung waved a hand with a solemn, dignified expression, then continued in his deep, weighty voice.

“Commander of the Jin Dragon Squad. And Old Master Jang. You’ve both had a difficult journey.”

“Not at all, my lord.”

“This old man is nothing to concern yourself with, Lesser Family Head.”

Wipeng was obviously a trusted retainer, but even Jang Taebo, who called me this brat and that bastard, was unfailingly respectful toward Jin Wikyung.

He had said he retired a long time ago. Had he taken on some subcontracting work for the Jin Family while I was away?

Ignoring my question, Jin Wikyung spoke again.

“The journey must have been tiring. Let’s all move somewhere else first.”

It wasn’t difficult to realize that I was included in that “all.”

It was equally obvious that the man running toward us over there, panting heavily, was not.

“Hyuk Mujin, Vice Commander of the Jin Dragon Squad! I have just completed my guard duty and returned!”

“……”

Some guard duty.

If you’re going to lie, wipe the sleep from your eyes first, you bastard.
```
