<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0960.txt",
      "sha256": "4271904b5f17d46ed4af9e916b9ab9af4c0a59e4ca03689b2335f976aa94bb42",
      "bytes": 13258
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d3429a1fe76bfb450f5253562f73acbcb3ec024cc9baecbfb3d719c555730feb",
      "bytes": 2089
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "ff5b5206798ca2c45ec6dcc084fc376e02e91696419ae72ce39f481882b60323",
      "bytes": 235018
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "88cbb2bdc825ac8486ce9f2ada2409a02608702fb8d332dbcba3d86f86765f3f",
      "bytes": 1007
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "541cb0aa807eab47bc9dd87a31ca1fb0862179f2714e0f1c7c7264366b26d9a6",
      "bytes": 1325
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "b07891412aaa7fe00333b7fca3c23629064cb88e839619ccc23b3be836cf3c21",
      "bytes": 759
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "90fee0d5c4549e3ba9bd9cf7e43854c53ffb7059e2feeedeff18016dcf6343aa",
      "bytes": 838
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "55815caedb05051398cae10cdb89ad1ade061f61f515737883b02030d0cb066e",
      "bytes": 1343
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "dd6272200a6db7fad1f2aec46a1d9975e485b419a455d74fd2c4785de73b20a6",
      "bytes": 1481
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "8eae4d67fdb4cbdb46a02f57e9d6c00ed476a19c03efeb95a22e4aa11a44fc20",
      "bytes": 622
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "0e0433c158e139b3a12acfda016481c944c34be25cac1538c544084fed8df66d",
      "bytes": 954
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ae380d93c75553af72479e87151ad9e37a2657326197311b6ef472e0603f3571",
      "bytes": 268838
    }
  ],
  "estimated_tokens": 11704
}
-->

# Durable State Update — Chapter 960

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
1 and safe_through 960. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 960. Profile updates may replace only one
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
  "chapter": 960,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 960,
    "continuity_sources": [960],
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
    "The battle at Eight Spring Gorge has resumed; Jin Mukyung, Jin Wikyung, Wipeng, and Cheol Mubaek face the Demon Bird.",
    "The real Chinggen is dead; the impostor who wore his face is the Demon Bird, an elderly and overwhelmingly powerful martial artist who left Temur alive to control the western tribes.",
    "The Dongting Fisherman died fighting the impostor. Jin Wikyung considers the Jin Family indebted to him and the other fallen.",
    "Jamukha ordered the Keshik at the gorge to wear down the defenders while limiting losses to his personal guard; three of his commanders of a hundred have died.",
    "Temur chose survival over loyalty and feels guilty that his actions led his followers to slaughter; Jamukha threatened him into obedience.",
    "The Emperor remains gravely ill with Blood Soul Gu; saving him requires him to die once, and Taekyung’s treatment remains unresolved.",
    "Jang Sam remains unconscious after his sudden rise in level and attack on Taekyung; the improved Temporary Strength Pill’s source, effects, and distribution remain unknown.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained.",
    "Taekyung resolved to trust his allies rather than bear every burden alone."
  ],
  "continuity_sources": [
    958,
    959
  ],
  "open_questions": [
    "How will the battle at Eight Spring Gorge end, and can the defenders defeat the Demon Bird?",
    "Who gave Jang Sam the silk pouch, and what are the improved pill’s effects and distribution?",
    "What is the Martial God’s identity and connection to the chosen one and the Bow Saint?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain?",
    "What will become of Temur and the followers he led into battle?"
  ],
  "safe_through": 959,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 철무백    | **Cheol Mubaek**   |
| 청풍     | **Cheongpung**     |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기연     | **fortuitous encounter**                         | Use sparingly                                         |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 선배     | **Senior**                                   |
| 일격     | **One Strike**                         |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 무형지독 | **Formless Ultimate Poison** | Unidentified poison discovered inside Jeok Cheongang's body. |
| 일다경 | **the time it takes to drink a cup of tea** | Duration in the progression of Jeok's lost time. |
| 소평 | **So Pyeong** | Alliance office worker assigned to prepare a report. |
| 케식 | **Keshik** | Elite warriors serving the Golden Clan. |
| 검귀 | **Sword Demon** | Title used for the kind of swordsman Mukyung is said to resemble. |
| 마조 | **Demon Bird** | Title given by the revealed impostor who wore Chinggen’s face. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 위팽 | 진태경 | retainer_to_third_young_master | Third Young Master | formal-polite and admonishing | Uses 삼공자 while warning Taekyung to return by noon and behave respectfully toward Jang Taebo. |
| 위팽 | 청풍 | Jin Family retainer to visiting Huashan martial artist | Young Hero Cheongpung | formal-polite and worried | Uses 청 소협 while warning that Cheongpung's refusal of the Sect Leader's order could strain relations between the Jin Family and Huashan. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 동정어옹 | hostile interrogator confronting a suspected perpetrator | you | blunt informal and abusive | Taekyung addresses the Dongting Fisherman without honorifics and calls him a sibu-leol bastard. |
| 기자 | 진태경 | Japanese reporter to celebrated foreign Hunter | Jin-sama | formal and reverent | Japanese reporters repeatedly address Jin with the honorific 사마. |
| 진태경 | 기자 | Hunter to Japanese reporter | reporter; you | blunt and insulting | Jin rebukes a reporter for talking back after criticizing Yamamoto's delayed arrival. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 959
- **Aliases:** Tiger of Mount Heng
- **Role:** Cheol Mubaek is the ninth-generation successor of the Shura Annihilating Fist and the Peak master known as the Tiger of Mount Heng, now out of seclusion and active in the rebuilding of the Mount Heng Sword Sect.
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** Close friend and peer of Lee Cheonbaek; paternal uncle and protector of Lee Seowol; considers Jin Taekyung, Jin Mukyung, and Hyuk Mujin Benefactors for protecting Seowol and enabling the Mount Heng Sword Sect's survival, and vows to repay them even at the cost of his life; feared and respected by the Mount Heng Sword Sect's senior figures

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 952
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 959
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 959
- **Aliases:** None
- **Role:** The Dongting Fisherman was an unaffiliated previous-generation Supreme Peak master whose water arts rivaled the Seafaring King; he died fighting the Jin Family of Taiyuan’s enemies at Eight Spring Gorge.
- **Personality:** The Dongting Fisherman is fiercely confident and sardonic, and he is determined to repay the Jin Family of Taiyuan and avenge himself on Dark Heaven.
- **Voice:** He speaks in measured, old-fashioned phrasing, calling himself 노부 and using fishing metaphors in dry taunts.
- **Relationships:** The Dongting Fisherman risked his life for the Jin Family of Taiyuan, which now considers itself indebted to him; he sought revenge on Dark Heaven.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 959
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Peak-level swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and seeks strength in service of his family.
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, and Mukyung cherishes his promise to reunite with him.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 955
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and learning to trust his allies rather than carry every burden alone.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 955
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 959
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and Commander of the Jin Dragon Squad; one of the Jin Family’s three Peak masters
- **Personality:** Loyal, observant, teasing, capable, and resigned to Jin Wikyung’s impulsive behavior. Respects the dead and urges others to live on their behalf.
- **Voice:** Weary and knowing, with dry humor when addressing Jin Wikyung or Jin Taekyung. Uses Sound Transmission when appropriate.
- **Relationships:** Trusted guard and retainer of Jin Wikyung; a reliable senior ally of Jin Taekyung. He has fought beside the Jin Family in major battles, including the conflict with Mount Heng, and remains alert to threats connected with Dark Heaven. The Human Butcher has claimed him as a personal target in a planned attack.

## Korean source

```text
＃960화



일다경(一茶頃).

고작 차 한잔 마실 시간이 흘렀을 뿐이었지만, 마조(魔鳥)는 내심 인정하지 않을 수 없었다.

자신이 눈앞의 먹잇감들을, 아니 산서인들을 과소평가했다는 사실을.

“발시(發矢)하라!”

쉬쉬쉬쉬쉭!

절벽을 저지한 것으로 끝이 아니었다.

협곡 입구 어림에 세워진 다섯 개의 토성(土城).

아직은 불완전한 흙과 바위의 성루에는 적지 않은 숫자의 궁수가 대기 중이었고, 날카로운 외침과 함께 쏟아진 화살 비는 한 덩어리가 되어 뒤엉키려던 사람들의 머리 위로 쏟아졌다.

정확히는, 협곡을 통과하기 위해 쉴 새 없이 밀려들던 초원의 군세를 향해.

쐐액! 푸푸푸푹!

“끄아아악!”

“내, 내 눈! 눈!”

사방에서 솟구치는 비명과 핏물.

급소에 화살을 맞은 유목민들이 몸부림친다.

물 흐르듯 이어진 몇 차례의 일제사격으로 빽빽하던 진형에 공백이 생기자, 태원진가를 필두로 한 산서인들은 송곳처럼 그 틈새를 파고들었다.

“쳐라!”

“와아아아아!”

돌파하려는 자와 막으려는 자.

두 갈래로 나뉜 인(人)의 파도는 서로를 향해 나아갔고, 그 충돌의 시작에는 새하얀 포말이 아닌 붉은 핏물이 기다리고 있었다.

카각! 콰드드득!

퍼걱!

강철과 강철이 맞물리며 불꽃을 피워올린다.

한 유목민이 내뻗은 날카로운 돌격창이 관군의 가슴팍을 관통했고, 힘없이 허물어지는 그의 시체를 뛰어넘은 태원진가의 무인은 유목민의 목젖을 베었다.

서걱!

“크륵, 컥!”

곳곳에서 넘쳐흐르는 비명과 신음.

모든 이가 끊임없이 서로를 죽이고, 죽었다.

지금 이 순간, 그들이 서 있는 이 전장에는 인간으로서 지녀야 할 일말의 자비나 동정 따위는 존재하지 않았다.

약육강식(弱肉强食).

약자는 결코 살아남을 수 없는 곳.

그것이 바로 전장이었고, 이 끔찍한 살육의 중심에 선 마조는 지난 수십여 년간 잊고 있던 즐거움을 다시 한번 느끼고 있었다.

“그래! 더, 더!”

그는 크게 소리 내어 웃으며 두 자루의 검을 휘둘렀다.

거칠 것 없던 지난날의 모습처럼.

정마대전(正魔大戰)이라 불린 그 거대한 전쟁에서, 마음껏 적의 목숨을 취하고 피를 들이켰던 자신의 과거를 떠올리며.

슈화악!

바람이 갈라진다. 길고 짧은 두 자루의 검에서 솟구친 강기(罡氣)가 공간을 베어 가르며 가장 먹음직스러운 먹잇감들을 향해 치달았다.

“산(散)!”

쉬잉!

거의 동시였다.

선두에 선 진무경이 벼락같은 외침을 토해 낸 것도.

그 외침이 울려 퍼짐과 동시에 항산호 철무백과 귀검 위팽이 몸을 비틀어 낸 것도.

그리고.

서걱!

그들을 아슬아슬하게 스쳐 지나간 붉은 강기가, 표적의 근처에 자리 잡았던 운 없는 자들을 휩쓸어 버린 것도.

푸화아아악!

비명은 없었다. 토막 난 육신과 피 분수만이 남았을 뿐.

“으아, 으아아아!”

두려움에 찬 누군가의 비명은, 삼십여 명에 달하는 관군과 무림인들이 어떤 최후를 맞이했는지 알려 주는 단서에 불과하다.

찰나의 순간.

단 한 번의 휘두름으로 자그마치 수십의 목숨이 사라졌다.

아니, 지워졌다.

마치 처음부터 존재하지 않았던 것처럼.

그것만이 당연한 운명인 것처럼.

‘이것이 초절정 고수……!’

위팽과 철무백은 자신들도 모르게 등골이 서늘해지는 것을 느꼈다.

절정과 초절정.

고작 한 글자가 더해졌을 뿐이지만, 이 두 경계선에 존재하는 벽은 너무나도 높고 거대했다.

지금으로부터 약 반년 전.

뜻하지 않게 태원진가의 문객이 되었던 또 다른 초절정 고수의 존재가 아니었다면, 그들은 조금 전의 일격을 본 것만으로도 전의를 상실해 버렸을지도 몰랐다.

‘하지만…… 그토록 강했던 노 선배께서도 결국 저놈에게 당했다.’

비록 동정어옹이 병상을 떨치고 일어난 지 얼마 되지 않았다는 것을 감안하더라도 마찬가지다.

지난 몇 달에 걸쳐 동정어옹의 가르침을 받았던 두 사람은 누구보다 잘 알고 있었다.

그가 어느 정도의 강자인지.

그 정도 수준의 고수가 건네는 말 몇 한마디와 수시로 벌어졌던 지도대련이 얼마나 대단한 기연(奇緣)인지.

동정어옹은 미쳐 날뛰던 자신을 저지해 준 것으로도 모자라 회복에 힘써 준 태원진가의 형제들에게 늘 감사함을 지니고 있었고, 그가 베푼 호의를 통해 태원진가의 전력은 비약적으로 상승할 수 있었다.

한데, 그랬던 그가 죽었다.

단 한 사람에 의해.

아니, 도무지 인간 같지도 않은 괴물에 의해.

그리고 늙은 낚시꾼을 씹어 삼킨 그 괴물은, 이제 자신을 향해 달려드는 새로운 사냥감을 향해 아가리를 벌리고 있었다.

바로 지금 이 순간에도.

쉭.

미세한 파공성과 함께 갈라지는 공간.

어둠 속에서 붉은 섬광이 번뜩인 그 순간, 위팽과 철무백은 온 힘을 다해 신형을 뒤집었다.

피핏!

뜨겁다.

분명 한 뼘 차이로 공격을 피했음에도, 압력을 이기지 못한 목덜미의 살갗이 갈라진다.

그러나 불현듯 찾아온 그 아릿한 통증은, 혼잡하던 머릿속을 오히려 차갑게 식혀 주었다.

‘이건…….’

잠시 크게 뜨였던 위팽과 철무백의 눈동자가 이내 깊게 가라앉았다.

지금의 회피는 단순한 우연이나, 본능에 따른 움직임이 아니다.

동정어옹과의 대련을 통해 익힌 감각과 기술. 그 외의 모든 것이 합쳐져 만들어 낸 결과물이다.

그리고 몇 달에 걸쳐 있었던 그 수많은 대련의 절반은, 두 사람의 합공(合攻)으로 이루어진 것이었다.

‘할 수 있다.’

이제는 눈빛만 보아도 안다.

스치듯 허공에서 교차한 시선과 함께, 위팽과 철무백의 신형이 동시에 흐릿해졌다.

파팟!

그들은 좌우로 나뉘어 쏘아졌다. 피로 물든 아수라장 속에서 서로를 향해 날붙이를 휘두르는 적아(敵我)를 뛰어넘어, 가파른 암벽을 밟으며 내달렸다.

동정어옹의 그것보다 빠르고 강한 괴물의 강기를 온 힘을 다해 피해 내며.

서걱, 콰아아앙!

수백 여년에 걸쳐 형성되었을 단단한 암벽이 두부처럼 갈라지고, 그 안으로 스며든 막강한 기운이 사방을 찢어발겨도 위팽과 철무백은 멈추지 않았다.

아니, 멈출 수 없었다.

눈앞의 적을 쓰러트리지 못한다면 모든 것이 끝장이었으니까.

두려움을 이기지 못하고 물러서거나, 줄어드는 거리만큼 늘어나는 크고 작은 상처 따위에 주춤했다가는 자신들보다도 한발 앞서 나아가고 있는 저 청년을 볼 면목이 없으니까.

‘이 공자.’

‘진천검(振天劍).’

지금 이 순간, 위팽과 철무백은 똑똑히 보고 있었다.

쉼 없이 빗발치는 강기의 소나기 속에서, 망설임 없이 적을 향해 달려드는 진무경의 모습을.

옅은 핏물을 흩뿌리면서도 한 치의 흔들림조차 느껴지지 않는 그의 단단한 등과 두 다리를.

더불어 문득 생각했다.

빛도 들지 않는 어둠을 벗어나 비로소 세상 밖으로 나온 그가.

진태경과 청풍이라는 그늘에 잠시 가려져 있던 또 한 명의 천재가 이 년이라는 시간을 어떻게 보냈을지.

그리고 마침내, 보았다.

스아아.

새하얀 검신을 타고 미끄러지는 달빛.

아니, 위팽과 철무백의 그것보다 더욱 휘황한 빛을 내뿜는 거대한 검기(劍氣)를.

쉬익.

느려진 세상 속.

비스듬히 내리그어진 푸른 검기가, 마조의 붉은 강기와 맞닿았다.



* * *



콰아아아앙!

그건 일순간 모두의 손발을 멈추게 만든 폭발이자, 협곡을 떨어 울리는 충격이었다.

그와 더불어, 폭발의 중심에 선 누군가에게는 기쁨과 경악이기도 했다.

콰아아아.

“으하, 으하하하하!”

사방으로 비산 하는 암석의 파편과 뿌옇게 솟아오른 먼지구름 너머, 실성한 사람처럼 미친 듯이 웃어젖히던 마조는 벼락처럼 손을 내뻗었다.

퍼엉!

압축된 공기가 터져나가며 드러난 시야, 일장에 걸쳐 깊게 파인 고랑 끝에 선 진무경의 모습을 본 마조가 누런 이빨을 드러냈다.

“이런, 이런 천하의 발칙한 놈을 보았나!”

막강한 살기와 기쁨이 뒤섞인다. 양손에 쥔 두 자루의 검이 파르르 떨리는 이유는, 비단 그가 느끼고 있는 감정뿐만이 아니었다.

툭.

자신의 발뒤꿈치에서 전해지는 단단한 감촉의 정체를, 마조는 이미 알고 있었다.

그것은 바위였다.

조금 전만 하더라도 세 걸음 뒤에 있었던, 그러나 이제는 그와 맞닿게 된 바위의 파편.

핏물에 흠뻑 젖은 가죽신으로부터 느껴지는 그 특유의 강도와 서늘함이, 마조로 하여금 미소 짓게 만드는 가장 큰 이유였다.

“기억도 나지 않는군. 누군가를 상대로 물러선 적이 언제였는지.”

맞다.

다가온 것은 바위가 아니다.

마조가, 자신이 물러난 것이다.

아니, 정확히는 물러나게 만들었다.

고작 이립도 되지 않은 핏덩이가, 정마대전부터 지금까지 피로 물든 일생을 살아온 늙은 노괴(老怪)를.

비록 세 걸음과 일장의 격차는 컸으나, 그런 사소한 것 따위는 마조에게 있어 아무것도 아니었다.

그는 똑똑히 보았다.

각기 다른 두 줄기의 검기와 강기가 맞닿기 직전, 저 핏덩이의 손끝에서 펼쳐진 아름다운 궤적을.

바다처럼 푸르렀던 그 빛을.

“그래, 그랬군.”

철벅.

마조가 천천히 내디딘 걸음이 피 웅덩이를 밟았다.

비대한 체구를 증명하듯, 그의 무거운 발걸음을 따라 핏물이 흘러넘쳤다.

“내심 희한했었지. 동정어옹, 그 늙은이와 싸우면서도 얼굴 한번 보지 못한 네놈의 모습이 눈앞에 어른거리는 이유가 무엇인지.”

며칠 전, 그는 선봉대의 전멸 소식과 함께 전령이 가져온 케식 백인장의 수급에서 검귀(劍鬼)의 흔적을 보았다.

“그것을 처음 본 그 순간부터 흥미가 동했다. 그만큼 완벽한 솜씨였으니.”

모든 것은 흔적을 남긴다.

짐승도, 인간도, 그리고 무공도.

각자의 죽음에는 저마다의 이유가 있고, 무림인의 경우라면 더더욱 그렇다.

그리고 소름 끼치도록 매끄러운 수급의 단면을 보며, 마조는 지난 수십여 년간 차갑게 식어 있던 피가 끓어오르는 것을 느꼈다.

오래전 명맥이 끊겼다고 알려진 신공절학(神功絶學)의 흔적을 발견해서?

혹은 자신과 비견될 만한 강자의 솜씨를 느껴서?

틀렸다.

동정어옹이라는 초절정 고수를 상대하면서도 검귀의 존재를 머릿속에서 지우지 못했던 이유를, 마조는 이제야 비로소 깨달았다.

“일격(一擊).”

수백, 수천 번을 보더라도 군더더기 없는.

실로 눈부시고, 아름답기까지 한.

그야말로 완벽한 일격.

바로 그 단 한 번의 움직임.

눈앞의 젊은 검귀는 그것을 지니고 있었다.

수 갑자의 공력을 가진 것도, 천하를 오시할 만한 신공절학을 익힌 것도 아니다.

다만, 무색(無色)하고도 무취(無臭)했다.

그렇기에 그 무엇보다 치명적이었다.

마치 손 쓸 새도 없이 누군가의 생명을 집어삼키는 무형지독(無形之毒)처럼.

어둠 속에서 은밀히 다가와 목을 베어 버리는 살수처럼.

“놀랍군. 아니, 경이로워.”

진심이 담긴 탄성과 함께 진무경을 바라보는 마조의 눈에는, 일말의 후회와 안타까움마저 깃들어 있었다.

“어째서, 왜 너 같은 놈을 지금 만난 거지?”

퉤.

검붉은 피가래를 뱉어 낸 진무경이 담담한 목소리로 말을 이었다.

“훨씬 일찍 만났어도, 너 같은 비루먹은 돼지 새끼를 스승님이라고 부를 일은 없었을 거다.”

위팽, 철무백과 함께 포위하듯 다가오는 그를 향해 마조는 안타까운 한숨을 내쉬었다.

‘왜, 왜 하필 지금이란 말이냐!’

일 년. 아니 삼 년만 늦게 만났다면 정말 기쁨으로 전신이 떨릴 만큼 좋은 승부를 낼 수 있었을 것이다.

지금 진무경의 앞에는, 반쯤 무너진 벽만이 존재할 뿐이니까.

하지만…….

그 기쁨의 순간은 두 번 다시 오지 않는다.

진무경은 오늘 이 자리에서 살아남을 수 없을 테니.

“안타깝구나. 진심으로.”

스아아아.

마조의 전신에서, 붉은 혈광이 피어올랐다.
```

## Final English reading copy

```markdown
# Chapter 960

The time it takes to drink a cup of tea.

Though only that much time had passed, the Demon Bird couldn’t help but admit it.

He had underestimated the prey before him—or rather, the people of Shanxi.

“Loose!”

*Fwish-fwish-fwish-fwish!*

Holding back the cliff wasn’t the end of it.

Five earthen fortifications stood near the entrance to the gorge.

Their ramparts of earth and rock were still incomplete, but a considerable number of archers waited behind them. At a sharp cry, a rain of arrows poured down over the heads of the people who had been crowding together into a single mass.

More precisely, it fell on the steppe forces that had been surging without pause toward the gorge’s passage.

*Fwoosh! Thud-thud-thud!*

“Aaagh!”

“M-my eye! My eye!”

Screams and blood erupted all around.

Nomads struck in vital spots writhed in pain.

After several coordinated volleys flowed one after another like water, gaps opened in the once-dense formation. The people of Shanxi, led by the Jin Family of Taiyuan, drove into them like awls.

“Attack!”

“Waaaaah!”

Those trying to break through and those trying to stop them.

Two waves of people surged toward one another. At the point where they collided, there was no white sea foam—only red blood waiting for them.

*Clang! Krrrunch!*

*Thwack!*

Steel clashed against steel, sending sparks into the air.

A nomad’s sharp lance pierced a government soldier through the chest. A martial artist of the Jin Family of Taiyuan leaped over the man’s limp body and cut the nomad’s throat.

*Shhk!*

“Ghk—cough!”

Screams and groans spilled from every direction.

Everyone killed and died without pause.

At this moment, on this battlefield, there was no mercy or compassion to be found in anyone.

The strong devoured the weak.

A place where the weak could never survive.

That was the battlefield. And at the center of this terrible slaughter, the Demon Bird felt a pleasure he hadn’t known in decades.

“Yes! More! Give me more!”

Laughing loudly, he swung the two swords in his hands.

Just as he had in the days when nothing could stand in his way.

He remembered his past, when he had freely taken the lives of his enemies and bathed in their blood during the great war called the Great Faction War.

*Shwaaa!*

The wind split apart. Force surged from the long and short swords, cleaving through the air as it raced toward the most delectable prey.

“Scatter!”

*Whoosh!*

It happened almost at the same time.

Jin Mukyung, at the head of the line, shouted like a thunderclap.

As his cry rang out, the Tiger of Mount Heng, Cheol Mubaek, and the Ghost Sword, Wipeng, twisted their bodies aside.

And then—

*Shhk!*

The red Force barely missed them and swept away the unlucky men standing near its target.

*Fwoooosh!*

There were no screams. Only severed bodies and fountains of blood remained.

Someone’s scream of terror was the only clue to the fate of the thirty or so government soldiers and martial artists.

In the blink of an eye.

With one swing, dozens of lives vanished.

No—they were erased.

As if they had never existed at all.

As if that had been their natural fate from the beginning.

*So this is a Supreme Peak master…!*

Wipeng and Cheol Mubaek felt a chill run down their spines before they knew it.

Peak and Supreme Peak.

Only a single character separated the two, but the wall between those realms was immeasurably high and vast.

About half a year ago—

If another Supreme Peak master hadn’t unexpectedly become a retainer of the Jin Family of Taiyuan, they might have lost the will to fight just from seeing that attack.

*But even that Senior, who was so powerful, was ultimately defeated by that monster.*

That was true even considering that the Dongting Fisherman had only recently recovered enough to leave his sickbed.

The two men had received the Dongting Fisherman’s instruction over the past several months. They knew better than anyone how strong he was.

They knew how great a fortuitous encounter it had been to hear a few words from a master of his caliber and take part in the training bouts he held so often.

The Dongting Fisherman had always been grateful to the Jin Family brothers for stopping him when he had gone on a rampage and helping him recover. Thanks to the goodwill he had shown them, the Jin Family of Taiyuan’s strength had grown by leaps and bounds.

And yet he had died.

At the hands of one man.

No—at the hands of a monster who hardly seemed human.

And the monster who had chewed up and swallowed the old fisherman now opened his jaws toward the new prey charging at him.

Even now.

*Whish.*

With a faint sound, the air split.

The instant a red flash flickered in the darkness, Wipeng and Cheol Mubaek twisted their bodies with all their strength.

*Pipip!*

Hot.

Though they had dodged the attack by a mere handspan, the pressure had been enough to split the skin at the back of their necks.

But that sudden, stinging pain cooled their muddled thoughts.

*This is…*

Wipeng and Cheol Mubaek’s eyes, briefly wide with surprise, quickly settled into a steady gaze.

Their evasion hadn’t been a simple coincidence or an instinctive movement.

It was the result of everything they’d gained through their training bouts with the Dongting Fisherman—their senses, their techniques, and all the rest—coming together.

And half of those countless bouts over the past few months had been fought by the two of them together.

*We can do this.*

Now they could tell just from looking into each other’s eyes.

Their gazes crossed in the air for an instant, and Wipeng and Cheol Mubaek blurred at the same time.

*Fwap!*

They shot off in opposite directions. In the blood-soaked chaos, they vaulted over friend and foe, each swinging blades at one another, and raced along the steep rock face.

They put everything they had into dodging the monster’s Force, which was faster and stronger than the Dongting Fisherman’s.

*Shhk! KABOOM!*

The solid cliff face, formed over what must have been hundreds of years, split like tofu. The tremendous energy that seeped into it tore everything around it to shreds, but Wipeng and Cheol Mubaek didn’t stop.

No—they couldn’t stop.

If they failed to defeat the enemy before them, everything would be over.

If they retreated out of fear, or hesitated over the large and small wounds multiplying as the distance between them closed, they wouldn’t be able to face the young man charging ahead of them.

*Second Young Master.*

*Heaven Shaking Sword.*

At this very moment, Wipeng and Cheol Mubaek could see him clearly.

Jin Mukyung, charging toward the enemy without hesitation amid the endless shower of Force.

His sturdy back and legs showed no hint of wavering, though flecks of blood scattered around him.

They suddenly wondered how he had spent those two years before finally emerging from that lightless darkness into the world.

How the other genius, who had briefly been overshadowed by Jin Taekyung and Cheongpung, had passed that time.

And then, at last, they saw it.

*Hssss.*

Moonlight slid along the white blade.

No—a massive Sword Energy shone even brighter than Wipeng’s and Cheol Mubaek’s.

*Whish.*

In a world that seemed to have slowed down,

the blue Sword Energy swept down at an angle and met the Demon Bird’s red Force.

* * *

*KABOOOOM!*

It was an explosion that brought everyone’s hands and feet to a halt in an instant—and a shockwave that shook the gorge.

For someone standing at the center of the blast, it also brought joy and astonishment.

*Rumble.*

“Ha! Hahahahaha!”

Beyond the fragments of rock scattering in every direction and the cloud of dust rising thick in the air, the Demon Bird laughed like a madman and thrust out his hand like a thunderbolt.

*Boom!*

The compressed air burst, clearing the view. Jin Mukyung stood at the far end of a deep furrow stretching a full *jang*. The Demon Bird bared his yellow teeth.

“Well, well! What a brazen little brat!”

Powerful killing intent mingled with delight. The two swords in his hands trembled—but not just because of what he was feeling.

*Tap.*

The Demon Bird already knew what the firm sensation against his heel was.

A rock.

A fragment of stone that had been three steps behind him just moments ago, but now touched his heel.

The distinctive firmness and chill he felt through his leather shoe, soaked in blood, were the greatest reason for his smile.

“I can’t even remember the last time I backed down from someone.”

That was right.

The rock hadn’t come to him.

The Demon Bird had retreated.

No—he had been forced back.

By a mere brat who wasn’t even thirty, against an old monster who had lived a life steeped in blood, from the Great Faction War to the present.

Though the distance of three steps and a *jang* was considerable, it meant nothing to the Demon Bird. He had seen it clearly.

Just before the two different streams of Sword Energy and Force met, the beautiful path traced by the brat’s fingertips.

That light, as blue as the sea.

“Ah, so that’s it.”

*Squelch.*

The Demon Bird stepped forward slowly, his foot sinking into a pool of blood.

The blood overflowed around his heavy step, befitting his immense frame.

“I always found it strange. Why your face kept appearing before me, even though I never saw you once while fighting that old man, the Dongting Fisherman.”

A few days ago, alongside news of the vanguard’s annihilation, a messenger had brought him the severed head of a Keshik commander of a hundred. On it, he’d seen the Sword Demon’s handiwork.

“The moment I first saw it, I became interested. The work was that perfect.”

Everything leaves a trace.

Beasts, people, and martial arts.

Every death has its own cause—and that is all the more true of Murim martial artists.

Looking at the chillingly smooth cut across the severed neck, the Demon Bird felt the blood that had been cold for decades begin to boil.

Was it because he’d found traces of a divine art said to have disappeared long ago?

Or because he’d sensed a skill to rival his own?

No.

The Demon Bird had only now realized why he hadn’t been able to get the Sword Demon out of his mind, even while facing a Supreme Peak master like the Dongting Fisherman.

“One Strike.”

A strike without a single wasted movement, no matter how many hundreds or thousands of times you watched it.

Truly dazzling. Beautiful, even.

A perfect strike in every sense.

That single movement.

The young Sword Demon before him possessed it.

He didn’t have internal energy accumulated over several *jiazi*, nor had he mastered a divine art that could look down on all the world.

It was simply colorless and odorless.

And that made it more lethal than anything else.

Like the Formless Ultimate Poison, which swallowed a person’s life before they could do anything about it.

Like an assassin who crept through the darkness and cut a man’s throat.

“Amazing. No—extraordinary.”

Along with his heartfelt exclamation, the Demon Bird’s eyes held a trace of regret and sorrow as he looked at Jin Mukyung.

“Why? Why did I have to meet someone like you now?”

*Ptooey.*

Jin Mukyung spat out a clot of dark red blood and answered in an even voice.

“Even if I’d met you much earlier, there’s no way I’d have called a mangy pig like you my Master.”

Wipeng and Cheol Mubaek approached with him, moving to surround the Demon Bird. He let out a regretful sigh.

*Why? Why did it have to be now?*

If they had met a year—or even three years—later, they could have had a match so good it would have made his whole body tremble with joy.

But Jin Mukyung had only a half-collapsed wall ahead of him.

Still…

That moment of joy would never come again.

Jin Mukyung wouldn’t survive this place today.

“What a shame. Truly.”

*Hssss.*

Red light rose from the Demon Bird’s entire body.
```
