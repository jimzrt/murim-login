<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1030.txt",
      "sha256": "1ca48eea9058dcd6bbf7aa43555c974612891a119e3a897297b9928fb21eaebf",
      "bytes": 13522
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "bbb77b9430abf805344c4022374f46b04790d237cb406d53ea8a2363a3d1c66f",
      "bytes": 1182
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "76d0a37c1aa5dfb6083ce2c1215ed35be5cb24aa50cffc0ea9a215ecc6885156",
      "bytes": 239797
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "48bc17c0bd159de1f84081605eee8a26feae3784812dd58f59e4efda48d5137e",
      "bytes": 932
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "ca3fd539ffdaefbe30ea35f4c90964f82a26388e18efc26c0716d96ae365fd2f",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "b6985e011c7998eb00719ddc99f2cefdb7746aa4f0749c020ad2e2fe4eb5a714",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "142491059376fe97565f9227607d9da0537132fad762c18635d5a6332aed1080",
      "bytes": 1748
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "ec9336f2dc2d16673ab7fad50c3db39d7ddba0c7f30b5760cb95a68124cb3332",
      "bytes": 623
    },
    {
      "path": "characters/Lei Fei.md",
      "sha256": "81179c9658c2af07112fdfa30bf818c40ae3f5791c4e38cba89c1adb7ca7861f",
      "bytes": 893
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "aaa7f9f43b44fe27ae8d225c02d5a63820b15a0af3d983e7c35d087e282ab4d3",
      "bytes": 1069
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "03a1c1209fa03435949a49d66244a6dda23347dc500c510ad3bf1c1650d99d34",
      "bytes": 279013
    }
  ],
  "estimated_tokens": 12269
}
-->

# Durable State Update — Chapter 1030

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
1 and safe_through 1030. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1030. Profile updates may replace only one
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
  "chapter": 1030,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1030,
    "continuity_sources": [1030],
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
    "The Blood-Sword Demon Lord once served the Heavenly Demon as a favored guard dog and now serves the Lord of Heaven.",
    "The Blood-Sword Demon Lord killed a thousand people with a gesture and admires Jeok Cheongang for burning his attackers alive at Mount Jiuhua.",
    "Jin Taekyung has reached the realm of the Ten Kings and is recognized as its eleventh giant.",
    "The First Elder of the Three Elders of Tianshan is alive but gravely injured; Jin Taekyung killed the Second Elder, and Sama Pyo killed the Third.",
    "A force of riders identified by Taekyung as Death Knights has arrived as the armies converge at the Great Snow Mountain."
  ],
  "continuity_sources": [
    1028,
    1029
  ],
  "open_questions": [
    "When did Dark Heaven and the Lord of Heaven emerge, and did Dark Heaven cause the Great Faction War?",
    "Who were the thousand people killed by the Blood-Sword Demon Lord, and what became of the rest of the meeting party?",
    "What is the Lord of Heaven’s identity and purpose?",
    "What are the Death Knights, and who commands them?"
  ],
  "safe_through": 1029,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 열화문    | **Fire Gate Clan**               |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 사제     | **Junior Brother**                           |
| 선배     | **Senior**                                   |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 귀가      | **your family**                                                 |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레이페이 | **Lei Fei** | Concealed Chinese S-rank Hunter and head of the Public Security Armed Forces Department in Sichuan Province. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 설삼 | **snow ginseng** | Elixir compared with the chapter's three selected roots. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 허공답보 | **Stepping on Empty Air** | Technique that allows Jongni Chu to move through empty air as if climbing invisible stairs. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 천년설삼 | **Thousand-Year Snow Ginseng** | Secret Zhongnan Sect cargo; a fully digested specimen can grant a full jiazi of internal energy. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 삼노 | **Three Old Men** | Mocking designation used by the Western Heaven Demon Lord for the aged Qilian Three Fiends. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 답보 | **stagnation** | Taekyung's current lack of progress in martial arts. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 천산삼노 | **Three Elders of Tianshan** | The three former Demonic Cult fiends serving the Blood-Sword Demon Lord. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 레이페이 | former ally and fellow Hunter | Lei Fei | blunt and solemn | Jin addresses Lei Fei by name before telling him to rest. |
| 레이페이 | 진태경 | former ally and fellow Hunter | you | familiar and respectful | Lei Fei uses 자네 and 하게 while asking Jin to help him fulfill his final mission. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 사령관 | captor to captive undead commander | you | casual, mocking, and dismissive | Taekyung addresses the Skeleton Warlord informally while rejecting its pleas to turn back. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 혈검마군 | 삼노 | former Demonic Cult fiend to subordinate | Elder Three | familiar and contemptuous | Addresses the wounded elder as 삼노 while asking how he compares to the Fire King. |
| 혈검마군 | 적천강 | former opposing martial masters | Senior Jeok | respectful and familiar | Addresses Jeok as 선배 while teasing him. |
| 적천강 | 혈검마군 | former opposing martial masters | you; you bastard | blunt and hostile | Uses 너 and 네놈 while confronting him. |
| 혈검마군 | 진태경 | enemy addressing a younger martial artist | you | familiar and measured | Uses 자네 while praising and assessing Taekyung. |
| 진태경 | 혈검마군 | young martial artist confronting an enemy | you | casual and challenging | Questions when the Blood-Sword Demon Lord and the Lord of Heaven appeared. |
| 사마표 | 삼노 | enemy addressing an elder of the Three Elders of Tianshan | you | casual and taunting | Sama Pyo answers the Third Elder’s accusation and taunts him while attacking. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1029
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Contemptuous of his former master and certain of his new cause, he treats the weak with ruthless disdain yet takes sincere delight in being recognized and openly admires formidable opponents.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He once served the Heavenly Demon and now serves the Lord of Heaven; he has been ordered not to kill Jin Taekyung, and he admires Jeok Cheongang for burning his attackers alive at Mount Jiuhua.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1029
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1029
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1028
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1028
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lei Fei.md

# Lei Fei (레이페이)

- **Safe through:** Chapter 429
- **Aliases:** None
- **Role:** Lei Fei is a concealed Chinese S-rank Hunter and former head of the Public Security Armed Forces Department in Sichuan Province who recovered his human identity after becoming a level-120 undead Death Knight Lord and died fulfilling his final mission.
- **Personality:** Lei Fei's recovered memories show him as dutiful, honorable, family-oriented, and willing to serve as an unseen guardian.
- **Voice:** His human voice is formal and earnest, becoming warm and playful with family.
- **Relationships:** Wei Fenghu is his maternal uncle who raised him as a son; Lei Fei married an unnamed flower-shop owner and had a daughter, trained alongside Wu Heixing, and was corrupted by the Arch Lich before Jin Taekyung restored his identity.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1029
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and calculating, he is protective of Taishan and pragmatic in combat; he recognizes that his father's ruthless, survival-driven worldview shaped him, even as its influence weighs on him.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan and is Sima Gong's son and heir; his father's ruthless treatment of family shaped his rise and remains a source of inner constraint. He joined the Fire Dragon Pavilion intending to use Jin Taekyung, and Sima Gong has now ordered him to spy on Taekyung's group. He was Ju Hwaran's former fiancé in a political engagement and is openly hostile toward fellow member Song Ilseom.

## Korean source

```text
＃1030화



비상식이 상식을 침범한 지 오래였다.

법칙은 깨졌고, 진리는 허물어졌으며, 죽음이라는 단어는 헐값이 되었다.

적어도 어느 청년이 나고 자란 세상은 그런 곳이었다.

몬스터. 헌터.

게이트라 불리는 차원의 경계 속에서 서로를 죽고 죽이는 괴물과 인간들.

마나와 마력.

지구가 태곳적부터 간직하고 있던 진리를, 인류의 역사를 장식한 몇몇 천재들이 발견해 낸 법칙을 산산조각 내 버린 이적(異蹟)의 힘.

그리고, 지금까지도 끝나지 않는 전쟁.

청년은 그러한 세상의 일원이었다.

마법이라는 이름으로 땅거죽을 뒤집고, 화염과 번개를 쏟아내고, 중력을 거스르는 세상.

케케묵은 신화 속에서만 묘사되었던, 혹은 그 누구도 상상할 수 없던 흉측한 용모와 상상할 수도 없는 힘을 지닌 괴물들에 맞서 눈부신 오러(Auror)를 뿜어내는 헌터들.

인간은 적응의 동물이었다.

인류가 위대한 승리를 거둔 그날에 태어난 작은 아이가 서른을 바라보는 나이가 되었을 때, 대격변이라는 이름으로 세계를 뒤엎은 비상식은 새로운 상식으로 자리 잡았다.

또 다른 비상식이 모든 것을 변화시키기 전까지는.

한여름의 가파른 언덕 위, 고시원 앞 분리수거장.

그곳에 버려져 있던 커다란 고철 덩어리.

아니, 또 다른 세상의 입구였던 VR 캡슐.

가진 것 없던 한 청년은 그렇게 새로운 세계에 발을 디뎠다.

보이지 않는 장막 너머의 그곳에는 실로 많은 것들이 기다리고 있었다.

지금까지와는 다른 위기와 기회, 그리고 보상.

좋은 사람들과 인연을 맺었고, 수많은 적과 맞서 싸웠으며, 그로 인해 성장할 수 있었다.

그렇기에 청년은 간절히 바랐다.

이곳에서만큼은 별다른 일이 없기를.

그런 마음 때문에, 시간이 흐를수록 짙어지는 한 가지 의심을 애써 축소하고 외면해 왔을지도 몰랐다.

바로 지금 이 순간, 믿기 싫었던 진실을 마주하기 전까지는.

“데스 나이트(Death Knight)……?”

문득 벌어진 입술 사이로 흘러나온 넋 나간 음성.

청년은, 아니 진태경은 멍하니 고개를 들어 바라보았다.

자신이 내뱉은 단어에 스스로 사로잡힌 채.

바로 지금 자신의 눈앞에 놓인 믿을 수 없는 광경에 압도당한 채.

스아아아아.

눈 덮인 산맥 위로 드리워진 먹구름 밑, 거무스름한 안개가 번져 온다.

그리고 그 중심에는 소리 없이 허공을 밟으며 들이닥치는 일곱 마리의 유령마(幽靈馬)와 전신을 빈틈없이 감싼 갑주 대신 칠흑과도 같은 흑의(黑衣)를 걸친 일곱 명의 사내가 있었다.

아니, 익숙하기 그지없는 죽음의 기운이 있었다.

그 어떤 외형을 하고 있더라도 변하지 않는 본질.

깊고 끈적한 죽음의 기운과 냄새가 진태경의 모든 감각으로, 영혼으로 전해지고 있었다.

‘틀림없어.’

순간, 진태경은 자신도 모르게 몸을 떨었다.

그가 옳았다. 바로 놈들이다.

데스 나이트.

영혼을 대가로 안식을 포기한 죽음의 기사들.

이계(異界)의 비상식이, 다시 한번 상식을 침범하고 있었다.

그러나 지금 이 순간에도 서로를 향해 진군해 오는 두 갈래의 대군세 속, 그 사실을 알아차린 것은 진태경 한 사람뿐이었다.

“퇴각! 지금 당장 퇴각하……!”

슈확!

순간, 아군을 향해 외침을 토해 내던 진태경은 전신의 솜털이 곤두서는 듯한 감각을 느끼며 돌아섰다.

천 번, 아니 만 번도 넘게 반복했던 움직임.

다급하지만 더없이 능숙하게, 회전하는 그의 허리와 팔을 따라 검푸른 강기가 해일처럼 일어났다.

꽈앙!

거대한 굉음이 공간을 떨어 울린다. 창날과 맞닿은 채 부르르 떨리는 회백색 검신 너머, 피에 미친 대마두가 진태경을 향해 히죽 웃었다.

“지금이라도 순순히 투항하지 그러나.”

“그 말, 그대로 돌려주마.”

진태경이 한 대답이 아니다.

어느덧 한 줄기 섬광이 되어 혈검마군의 측면을 파고든 적천강의 일장(一掌)이, 나직한 음성을 앞질러 쏘아졌다.

화아악.

일순간 터져 나온 광염(光焰)은 눈부셨고, 동시에 뜨거웠다.

공기를 불사르고 만년설을 녹이는 화염신장(火焰神掌)의 끔찍한 열기 앞에, 혈검마군이 망설임 없이 몸을 비틀었다.

퍼엉!

압축된 공기가 폭발한다. 아니, 그대로 증발한다.

아슬아슬하게 장력을 피한 혈검마군은 땅을 박차며 뒤로 물러났다.

분명 나름대로 성공적이라고 할 만한 회피였음에도, 열기의 여파를 이기지 못한 옷깃과 그 너머의 살갗은 새카맣게 그을려 있었다.

“어이쿠. 이런.”

세상에 존재하는 그 어떤 고통보다 심하다는 것이 바로 작열통(灼熱痛)이다.

그러나 살갗이 그을리다 못해 일부가 녹아 문드러졌음에도, 혈검마군의 입가에는 여전히 웃음이 맺혀 있었다.

“역시 듣던 대로 화끈하시구려, 선배.”

“놈……!”

“그리 성내지 마시오. 내가 말은 이렇게 해도 내심 속이 쓰리거든.”

혈검마군의 말은 도발이 아니라 진심이었다.

단 한 번의 격돌이었지만 그는 확실히 느끼고 있었다.

이대로는 결코 혼자서 화왕 적천강을 쓰러트릴 수 없다는 사실을.

설령 자신보다 반 수 위의 고수인 그가 없다 해도, 진태경을 죽이지 않고 생포하는 것은 매우 어려운 일이 되리라는 것을.

물론, 이는 어디까지나 지금까지의 상황에 한해서였다.

“앞으로 벌어질 일에 대해 선배께 미리 양해를 구해야겠소. 아, 자네에게도 같은 마음일세. 나로서도 이런 방식이 조금은 마음에 들지 않지만…….”

짐짓 눈살을 찌푸렸던 혈검마군이, 이내 너털웃음을 터트리며 말을 이었다.

“뭐 어쩌겠나. 이 역시 그분의 위대함을 증명하는 과정인 것을.”

그 순간.

두두두두두!

어느덧 백여 장 앞까지 치달은 암천의 대군세가, 정확히는 그 수많은 광신도들의 필두에 선 일곱 쌍의 인마(人馬)가 허공을 밟으며 솟구쳤다.

아니, 달렸다.

쐐애애액!

그들과 대적하기 위해 진군해 오던 모두가 그 모습을 똑똑히 볼 수 있었다.

동시에 수만 쌍의 눈이 부릅떠지고, 굳게 닫혀 있던 입술이 저절로 열렸다.

경악. 두려움.

오직 두 가지 감정만이 그들의 눈동자와 얼굴에 드리워졌다.

이 광경을 무엇이라 불러야 할까.

허공답보(虛空踏步)? 혹은 능공허도(凌空虛道)?

그건 모두의 머릿속에 존재하는 그 어떤 단어도 쉽게 설명할 수 없는 것이었다.

허공답보를 펼칠 정도로 경신술이 뛰어난 고수들은 지금 당장 무림맹 측에도 몇 명이나 있었으나, 말과 함께 허공을 내달린다는 것은 상상해 본 적도 없는 기사(奇事)였으니까.

그러나 한 사람만큼은 달랐다.

‘놈들이, 온다.’

진태경은 백염을 그러쥐었다.

이 전장의 그 누구보다 커다란 충격을 받은 그였지만, 누구보다 현실을 직시하고 있는 이 역시 그였다.

익숙하면서도, 낯선 느낌.

현대에서는 데스 나이트라 불리고, 무림에서는 무엇이라 불러야 할지 모를 그것들은 눈부신 속도로 가까워지고 있었다.

‘강하다. 일반적인 놈들이 아니야.’

진태경은 직감했다. 달라진 것은 외형뿐만이 아니라는 것을.

가까워지는 만큼 짙어지는 죽음의 냄새와 기운은, 그가 알고 있던 일반적인 데스 나이트의 기준을 훌쩍 넘어선 것이었다.

‘그래, 이건 마치…….’

레이페이.

그리 오래되지 않은 과거, 아크 리치에 의해 강제로 영혼이 타락해버린 또 한 사람을 영웅을 진태경은 불현듯 떠올렸다.

‘데스 나이트 로드.’

레이페이는 S급 헌터이자 영웅이었지만, 타락한 상황에서의 그는 당시만 하더라도 아크 리치 다음으로 강력했던 적이었다.

데스 나이트 중에서도 선택받은, 생전의 힘을 고스란히 간직하다 못해 더욱 강해진 우두머리.

그야말로 로드(Lord)라는 칭호가 붙기에 한 치의 부족함도 없었던 네임드 몬스터.

그런데, 적들의 선두에서 유령마를 이끌고 들이닥치는 일곱 명의 흑의인들이 각각 뿜어내는 기세는 결코 그때의 레이페이에 비교해도 떨어지지 않았다.

‘아니, 그 이상.’

돌이키기에는 이미 늦었다.

공포와 두려움은 전염된다.

진태경이 천산삼노를 순식간에 쓰러트리는 광경을 멀찍이서 지켜보며 하늘을 찌를 듯했던 아군의 사기는, 듣도 보도 못한 광경 앞에서 물거품처럼 사그라지고 있었다.

‘아군 모두를 대설산에서 끌어낸 거야. 천산삼노를 일종의 제물로 삼아서.’

진태경은 그제야 깨달았다.

천산삼노는 처음부터 바로 이 시점을 위한 미끼로서 활용되었다는 것을.

그리고 그러한 혈검마군의 의도는 정확히 먹혀들었다.

설령 이대로 아군이 퇴각한다 해도, 놈들이 들이닥치는 속도가 더더욱 빠를 테니까.

결국 진태경에게 남은 것은 두 갈래로 나뉜 갈림길뿐이었다.

적과 병장기를 맞대기도 전에 흔들리는 아군의 퇴각을 위해 이 위치를 사수하든가.

혹은…….

‘모든 것을 걸고, 이 상황을 뒤집거나.’

그리고 지금 진태경의 곁에는, 그 누구보다 믿고 따를 수 있는 버팀목이 있었다.

“몇 놈 맡으실래요?”

“여덟 놈 전부.”

적천강의 담담한 대답에, 진태경이 피식 웃었다.

“힘드실 텐데. 나이가 있으셔서.”

“걱정 말거라. 회춘했더니 힘이 펄펄 솟는다.”

“전에 천년설삼 가져다 드린 보람이 있네요.”

“그걸 누구 코에 붙이라고. 다음에는 만년설삼으로 가져오너라.”

“양심 있으십니까?”

“열어서 확인해 볼 테냐?”

열화문의 두 사제(師弟)는 철탑처럼 전장의 중심에서 적들을 기다렸다.

오십여 장 밖, 한껏 상기된 얼굴로 이곳을 응시하는 혈검마군의 어깨너머로 새카맣게 몰려든 대군세가 자신들의 총사령관을 스쳐 그들을 향해 쏟아지고 있었다.

“개떼같이도 몰려드는군. 사파 놈들도 한 수 접겠어.”

적천강의 중얼거림에 이번에는 사마표가 실소를 흘렸다.

“예. 제 생각에도 그런 것 같습니다.”

“그러고 보니, 사파 핏덩이가 여기에도 한 놈 있었구먼.”

“부정은 못 하겠군요.”

“사파라, 네놈은 정녕 스스로를 그리 생각하느냐?”

“이 시점에 대답할 문제는 아닌 것 같지만, 어쩌겠습니까. 태어나 보니 온 천하가 저를 사파라 부르는 것을. 이게 제 팔자겠지요.”

삼십여 장.

온 사방을 떨어 울리는 적들의 함성에 귀가 먹먹해지는 것을 느끼며, 사마표가 한때 천산삼노의 것이었던 도검을 양손에 힘주어 그러쥔 그때였다.

“듣자 하니 어이가 없네. 병신이냐?”

귓가에 흘러들어오는 나직한 음성에, 사마표의 신형이 덜컥 굳었다.

“뭐……라고?”

“병신이냐고. 너.”

이십여 장.

수만 명의 적들이 뿜어내는 기세로 인해 떨리는 공기 속, 진태경은 평온한 목소리로 말을 이었다.

“태어난 대로 살고, 남들에게 불리는 대로 흘러가면 그게 네 인생이냐?”

“그건.”

“그냥 꼴리는 대로 살아. 지킬 거 지키고, 가끔은 착한 짓도 하고. 그러면 정파든 사파든 흑도든…… 그게 무슨 상관이냐.”

사마표의 얼굴이 딱딱하게 굳었다.

거침없는 언행.

그래서 더 아프고, 부럽다.

그와 달리, 진태경은 정도(定道)에서 태어났으니까.

“네가 뭘 안다고, 감히 그런 말을 하는 거지?”

“나야 당연히 좆도 모르지. 네가 어떤 인생을 살아왔는지 어떻게 알겠냐. 말해 준 적도 없는데.”

“뭐?”

“그래도, 네가 어떤 놈인지는 좀 알지.”

십여 장.

먹구름이, 어둠이 드리워진다.

텅 빈 허공을 밟으며 떨어져 내리는 그림자들을 노려보며, 진태경이 한 마디를 툭 내뱉었다.

“지금, 이곳에 같이 있으니까.”

“……!”

“내가 사람 보는 눈이 좀 있는 모양이야. 안 그래요, 노야?”

적천강은 대답하지 않았고, 진태경은 대답을 기다리지 않았다.

지금으로부터 약 일 년 전. 무작정 찾아온 흑룡마문의 소문주를 흔쾌히 일원으로 받아들였던 화룡각의 각주(閣主)는 손에 쥔 창을 휘둘렀다.

솨아악.

겁화처럼 뜨겁고, 벽력처럼 쾌속한 검푸른 해일이 일었다.

그리고 망설임 없이 나아가는 진태경을 보며, 사마표는 문득 생각했다.

그 모습이, 퍽 눈부시다고.

콰아아아앙!
```

## Final English reading copy

```markdown
# Chapter 1030

The day when common sense was invaded by the absurd had come and gone long ago.

Laws were broken, truths were torn down, and the word *death* had become cheap.

At least, that was the world in which one young man had been born and raised.

Monsters. Hunters.

Monsters and humans killing one another inside the boundaries between dimensions known as Gates.

Mana and magical power.

Miraculous forces that shattered the truths Earth had held since ancient times, and the laws discovered by a handful of geniuses who had shaped human history.

And a war that still hadn’t ended.

The young man was part of that world.

A world where people overturned the earth in the name of Magic, unleashed fire and lightning, and defied gravity.

Hunters who poured out dazzling auras as they faced monsters with grotesque forms and unimaginable strength—creatures described only in ancient myths, or beyond anything anyone could imagine.

Humans were adaptable creatures.

By the time the little child born on the day humanity won its great victory was approaching thirty, the absurdity that had overturned the world in the Great Cataclysm had become the new common sense.

That is, until another absurdity changed everything.

On a steep hill in the middle of summer, outside a goshiwon[^1], stood a recycling area.

A massive hunk of scrap metal had been dumped there.

No—it was a VR capsule, an entrance to another world.

With nothing to his name, one young man had stepped into that new world.

So much awaited him beyond the invisible veil.

Dangers and opportunities unlike any he’d known, and rewards.

He had formed bonds with good people, fought countless enemies, and grown because of it.

That was why the young man had wished so desperately for one thing:

That nothing out of the ordinary would happen here.

Perhaps that wish was why, as time passed, he kept trying to downplay and ignore the one suspicion growing stronger by the day.

At least, until this very moment, when he came face-to-face with the truth he didn’t want to believe.

“Death Knights…?”

The vacant words slipped from his lips.

The young man—or rather, Jin Taekyung—blankly lifted his head to look.

Entranced by the word he’d just spoken.

Overwhelmed by the unbelievable sight before his eyes.

Sssaaaaa.

Beneath the dark clouds hanging over the snow-covered mountains, a murky haze spread.

At its center, seven ghost horses soundlessly charged forward, stepping on empty air. On their backs sat seven men dressed not in armor that covered them from head to toe, but in black clothes as dark as pitch.

No—what he sensed was a presence of death as familiar as could be.

Its essence didn’t change, no matter what shape it took.

A deep, cloying aura of death, and its stench, seeped into every one of Jin Taekyung’s senses—even his soul.

*No mistake.*

For a moment, Jin Taekyung trembled without realizing it.

He’d been right. It was them.

Death Knights.

Knights who had given up their souls and forsaken their rest.

The absurdity of another world was invading common sense once again.

And yet, amid the two vast armies advancing toward each other even now, Jin Taekyung was the only one who had noticed.

“Retreat! Fall back, now—!”

Whoosh!

As he shouted at his allies, Jin Taekyung suddenly felt every hair on his body stand on end. He spun around.

A movement he’d repeated a thousand times—no, more than ten thousand.

Urgent, yet perfectly practiced, it followed the turn of his waist and arms. Dark-blue Force rose like a tidal wave.

KWAANG!

A deafening boom shook the air. Beyond the gray-white blade trembling where it met the spearpoint, a fiend gone mad with blood grinned at Jin Taekyung.

“Why not surrender while you still can?”

“I’ll return those words to you.”

The reply hadn’t come from Jin Taekyung.

Jeok Cheongang’s palm shot ahead of his quiet voice, flashing like a streak of light as it struck at the Blood-Sword Demon Lord’s flank.

Whooosh.

A blaze erupted in an instant, dazzling and scorching all at once.

Faced with the terrible heat of the Flame Divine Palm, which burned the air and melted ten-thousand-year snow, the Blood-Sword Demon Lord twisted aside without hesitation.

BOOM!

Compressed air exploded. No—it vaporized on the spot.

The Blood-Sword Demon Lord narrowly evaded the palm strike, leaping backward off the ground. It had been a successful dodge, by any measure, but the heat had still taken its toll. His collar and the skin beneath it were scorched black.

“Whoops. Well, look at that.”

Of all the pains in the world, burning pain was said to be the worst.

Yet even with his skin charred and parts of it melted into a mess, a smile still lingered on the Blood-Sword Demon Lord’s lips.

“Just as they said, you’re a fiery one, Senior.”

“You bastard…!”

“Don’t be so angry. I may speak this way, but it stings me too.”

The Blood-Sword Demon Lord wasn’t trying to provoke him. He meant it.

They’d clashed only once, but he’d felt it clearly.

He couldn’t defeat the Fire King, Jeok Cheongang, alone.

Even without Jeok Cheongang, a master half a step above him, capturing Jin Taekyung alive rather than killing him would be very difficult.

Of course, that was only true of how things stood now.

“I should ask your understanding in advance for what’s about to happen, Senior. And you as well, my friend. I’m not entirely fond of doing things this way, either…”

The Blood-Sword Demon Lord had furrowed his brow as if he were troubled, but soon he burst into hearty laughter and continued.

“What can you do? This, too, is part of proving that person’s greatness.”

At that moment—

Rumble, rumble, rumble!

The vast army of Dark Heaven had already charged to within roughly three hundred thirty yards. More precisely, the seven pairs of riders at the head of the countless fanatics rose into the air, stepping on empty space.

No—they ran.

Screee!

Everyone advancing to oppose them could see it plainly.

Tens of thousands of eyes widened. Lips that had been tightly shut fell open on their own.

Shock. Fear.

Only those two emotions showed on their faces and in their eyes.

What could they call this sight?

Stepping on Empty Air? Or Traversing the Void?

None of the words in anyone’s mind could easily explain it.

There were several masters on the Murim Alliance’s side who could use body-lightness techniques well enough to step on empty air. But no one had ever imagined running through the sky on horseback. It was an unprecedented wonder.

But one person was different.

*They’re coming.*

Jin Taekyung gripped White Flame.

He was more shocked than anyone else on the battlefield, yet he was also the one seeing reality most clearly.

A feeling both familiar and unfamiliar.

Called Death Knights in the modern world, these beings—whatever the Murim might call them—were closing in at blinding speed.

*They’re strong. Not ordinary ones.*

Jin Taekyung had sensed it. Their appearance wasn’t the only thing that had changed.

The closer they came, the stronger the stench and aura of death grew. They far surpassed the ordinary Death Knights he knew.

*Right, this is just like…*

Lei Fei.

Jin Taekyung suddenly remembered another hero, not so long ago, whose soul had been forcibly corrupted by an Arch Lich.

*The Death Knight Lord.*

Lei Fei had been an S-rank Hunter and a hero, but while corrupted, he had been the most powerful enemy around after the Arch Lich itself.

A chosen leader among Death Knights, one who’d kept all his strength from life—and grown even stronger.

A named monster who deserved the title of Lord without the slightest reservation.

But the seven men in black, leading ghost horses at the head of the enemy forces, each exuded an aura that was no weaker than Lei Fei’s had been.

*No. Stronger.*

It was already too late to turn back.

Fear was contagious.

The morale of Jin Taekyung’s allies, which had soared as they watched him defeat the Three Elders of Tianshan in an instant, was fading like a bubble before this sight no one had ever heard of or seen before.

*He drew the whole army out of the Great Snow Mountain. He used the Three Elders of Tianshan as bait.*

Jin Taekyung understood at last.

The Three Elders of Tianshan had been used as bait from the very beginning, for this exact moment.

And the Blood-Sword Demon Lord’s plan had worked perfectly.

Even if their allies retreated now, the enemy would reach them all the faster.

In the end, Jin Taekyung was left with only two paths.

Hold this position so their shaken allies could retreat before they even crossed weapons with the enemy.

Or…

*Risk everything and turn this around.*

And at Jin Taekyung’s side stood someone he could trust and follow more than anyone.

“How many will you take?”

“All eight.”

At Jeok Cheongang’s calm reply, Jin Taekyung gave a quiet laugh.

“That’ll be tough. You’re getting old.”

“Don’t worry. I’ve got energy to spare since I got younger.”

“I’m glad that Thousand-Year Snow Ginseng I brought you was worth it.”

“What was I supposed to do with that? Bring me Ten-Thousand-Year Snow Ginseng next time.”

“Do you have any shame?”

“Want to open me up and check?”

The Fire Gate Clan’s master and disciple stood at the heart of the battlefield like iron towers, waiting for the enemy.

About a hundred sixty-five yards away, the vast army that had gathered behind the Blood-Sword Demon Lord—whose face was flushed with excitement as he stared at them—surged past its commander and poured toward them.

“They’re swarming like a pack of dogs. Even the unorthodox faction would be impressed.”

At Jeok Cheongang’s mutter, Sama Pyo gave a dry laugh.

“Yes. I think so too.”

“Come to think of it, there’s one unorthodox brat right here.”

“I can’t deny that.”

“The unorthodox faction, is it? Do you truly think of yourself that way?”

“It doesn’t seem like the time for that question, but what can I do? I was born, and the whole world called me unorthodox. I suppose that’s just my lot.”

About a hundred yards.

The enemy’s shouts shook the air from every direction, making their ears ring. Sama Pyo tightened his grip on the sword and saber that had once belonged to the Three Elders of Tianshan, one in each hand.

“Listening to that is ridiculous. Are you an idiot?”

At the quiet voice in his ear, Sama Pyo’s body stiffened.

“What… did you say?”

“I asked if you’re an idiot. You.”

About sixty-five yards.

With tens of thousands of enemies making the air tremble with their auras, Jin Taekyung continued in a calm voice.

“You live the way you were born, let other people decide what to call you, and just go along with it—is that your life?”

“That’s…”

“Just live however the hell you want. Protect what matters to you. Do something good now and then. Then what does it matter if you’re orthodox, unorthodox, or part of the dark-path figures?”

Sama Pyo’s face went stiff.

Those unrestrained words.

That made them hurt all the more—and made him envy Jin Taekyung.

Unlike him, Jin Taekyung had been born with a path already laid out for him.

“What do you know about me to say something like that?”

“Of course I don’t know shit. How would I know what kind of life you’ve lived? You’ve never told me.”

“What?”

“But I know what kind of person you are.”

About thirty yards.

Clouds gathered; darkness fell.

Watching the shadows descend through the empty air, Jin Taekyung tossed out one short sentence.

“We’re here together now.”

“……!”

“I guess I’m pretty good at judging people. Right, Old Master?”

Jeok Cheongang didn’t answer, and Jin Taekyung didn’t wait for one.

About a year earlier, the Pavilion Master who had gladly accepted the Young Sect Leader of the Black Dragon Demon Gate when he’d come calling out of the blue swung the spear in his hand.

Whooosh.

A dark-blue tidal wave surged up, hot as hellfire and swift as a thunderbolt.

And as Jin Taekyung advanced without hesitation, Sama Pyo suddenly thought:

He looked dazzling.

KWA-BOOM!

[^1]: A goshiwon is a very small, inexpensive room-for-rent arrangement in South Korea.
```
