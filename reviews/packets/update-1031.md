<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1031.txt",
      "sha256": "617b28eaba5ca98ba15bcdd2f4647ba7a1296e93a4d19abbfe15da32920ca9a2",
      "bytes": 12417
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ce3b874457bc7a742de1e0504b781daf0faf4c7f4efdc86f05ab013f0c912b62",
      "bytes": 1013
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "76d0a37c1aa5dfb6083ce2c1215ed35be5cb24aa50cffc0ea9a215ecc6885156",
      "bytes": 239797
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "b20d02548f19c06cc53f503be18b1809c1ad0a710adfee7b34465d64b645f06b",
      "bytes": 932
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "39ae11eedcd89008133acd5bc6b410339a07dbdc5605d3c05f92b0778ff25aac",
      "bytes": 1502
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "6c184c3205fd2e99478e23007e1b5f4b857f8b7eb1fe8489488399415e0c4c98",
      "bytes": 1001
    },
    {
      "path": "characters/Qilian Three Fiends.md",
      "sha256": "d9ab353caa198f9bc1ae6651de43630456d104a55335f032480c626a41d9162d",
      "bytes": 637
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "dda0f2b255d4a7f1f8812dcf324219fdf0efc0fbf17d4e8b8286a70bde912ec3",
      "bytes": 1161
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "1d8351d583536f370402bd609b54674959c846a55bebf468095c95126242c0ae",
      "bytes": 778
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "54a80c84932ca9e8e56cd726be585883c516a36bb057eca687b184dc83f8c568",
      "bytes": 686
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "f0f687045de7c31913291cc0da0dc0e5d4a2a1f99327e5c363416232ef6fe1cb",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "03a1c1209fa03435949a49d66244a6dda23347dc500c510ad3bf1c1650d99d34",
      "bytes": 279013
    }
  ],
  "estimated_tokens": 11628
}
-->

# Durable State Update — Chapter 1031

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
1 and safe_through 1031. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1031. Profile updates may replace only one
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
  "chapter": 1031,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1031,
    "continuity_sources": [1031],
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
    "The Blood-Sword Demon Lord serves the Lord of Heaven and used the Three Elders of Tianshan as bait to draw Taekyung’s forces out.",
    "Taekyung recognizes seven powerful black-clad riders on ghost horses as Death Knights; they seem at least as powerful as Lei Fei was as a Death Knight Lord.",
    "The allied army’s morale is shaken by the riders’ arrival as the enemy force advances.",
    "Taekyung, Jeok Cheongang, and Sama Pyo are together facing the advancing army.",
    "Taekyung tells Sama Pyo not to let his unorthodox label define him and considers him worth trusting."
  ],
  "continuity_sources": [
    1030
  ],
  "open_questions": [
    "Who are the seven Death Knights, what is their rank, and who commands them?",
    "What is the Lord of Heaven’s identity and purpose?",
    "When did Dark Heaven and the Lord of Heaven emerge, and did Dark Heaven cause the Great Faction War?"
  ],
  "safe_through": 1030,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 사마공    | **Sima Gong**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 종남파    | **Zhongnan Sect**                |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 일격     | **One Strike**                         |
| 사천     | **Sichuan**            |
| 감숙     | **Gansu**              |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 기련삼괴 | **Qilian Three Fiends** | Three identical brothers from the Qilian Mountains. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 삼괴 | **Three Fiends** | Collective form used by the Western Heaven Demon Lord for the Qilian Three Fiends. |
| 삼노 | **Three Old Men** | Mocking designation used by the Western Heaven Demon Lord for the aged Qilian Three Fiends. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 유령환살보 | **Ghost Illusory Slaughter Step** | Movement technique used by the Slaughter Saint. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 시산혈해 | **sea of corpses and blood** | Description of the preceding months of bloodshed. |
| 무량수불 | **Infinite Life Buddha** | Buddhist invocation used by Taekyung. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 서울 | **Seoul** | Location announced for the World Hunter Federation's inaugural ceremony. |
| 모산파 | **Maoshan Sect** | Jiangsu sect known for sorcery, destroyed by the founding emperor. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 천산삼노 | **Three Elders of Tianshan** | The three former Demonic Cult fiends serving the Blood-Sword Demon Lord. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 서천마군 | 기련삼괴 | commander_to_subordinates | Three Fiends; Three Old Men | mocking and superior | Calls them 삼괴 and then mockingly says they may now be called 삼노. |
| 기련삼괴 | 서천마군 | subordinates_to_commander | my lord | fearful and deferential | The brothers greet the Western Heaven Demon Lord as 마군. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 적천강 | 풍운검군 | legendary_elder_to_Zhongnan_sect_leader | Wind-and-Cloud Sword Lord | familiar and commanding | Jeok Cheongang tells him to get the Zhongnan disciples moving. |
| 노호검객 | 적천강 | senior_martial_artist_to_legendary_elder | Senior Jeok | deferential and cautious | Addresses Jeok as 노 선배 while explaining his actions. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 풍운검군 | 적천강 | Zhongnan Sect Leader to legendary martial master | Senior Jeok | respectful | Refers to Jeok as 적 대협. |
| 사마공 | 사마표 | father to son | Pyo | intimate and familiar | Sima Gong calls him 표야 and 내 아들아. |
| 풍운검군 | 노호검객 | Zhongnan Sect Leader to Senior Brother | Senior Brother | respectful and strained | Addresses him as 사형 while protesting the decision. |
| 풍운검군 | 태을무정검 | Zhongnan Sect Leader to Senior Brother | Senior Brother | respectful and strained | Addresses him as 사형 while protesting the decision. |
| 혈검마군 | 삼노 | former Demonic Cult fiend to subordinate | Elder Three | familiar and contemptuous | Addresses the wounded elder as 삼노 while asking how he compares to the Fire King. |
| 혈검마군 | 적천강 | former opposing martial masters | Senior Jeok | respectful and familiar | Addresses Jeok as 선배 while teasing him. |
| 적천강 | 혈검마군 | former opposing martial masters | you; you bastard | blunt and hostile | Uses 너 and 네놈 while confronting him. |
| 사마표 | 삼노 | enemy addressing an elder of the Three Elders of Tianshan | you | casual and taunting | Sama Pyo answers the Third Elder’s accusation and taunts him while attacking. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1030
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Contemptuous of his former master and certain of his new cause, he treats the weak with ruthless disdain yet takes sincere delight in being recognized and openly admires formidable opponents.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He once served the Heavenly Demon and now serves the Lord of Heaven; he has been ordered not to kill Jin Taekyung, and he admires Jeok Cheongang for burning his attackers alive at Mount Jiuhua.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1030
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 996
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu was the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family who died as his accumulated internal energy and remaining life force melted into the flames of Taekyung’s advancement.
- **Personality:** Boisterous and teasing with old friends, yet calm and accepting in the face of death; willing to give everything he has left to protect the world.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** He was Jeok Cheongang’s long-standing rival and friend, Hong Dao’s close friend, protective toward Hong Dao’s Disciple Unnamed, father of Peng Cheolyeong, and longtime friend and former youthful rival of Murong Baek; Jeok and Peng parted reconciled as brothers in all but blood.

### Qilian Three Fiends.md

# Qilian Three Fiends (기련삼괴)

- **Safe through:** Chapter 644
- **Aliases:** Three Fiends
- **Role:** First Fiend and at least one other brother are dead, the Third Fiend has been captured by Mungyeong, and the Second Fiend's fate remains unknown.
- **Personality:** Bloodthirsty and notorious throughout Qinghai, but fearful and submissive before the Western Heaven Demon Lord.
- **Voice:** The brothers speak in near-unison with frightened, deferential phrasing.
- **Relationships:** They serve the Western Heaven Demon Lord and address him as their superior.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1030
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and calculating, he is protective of Taishan and pragmatic in combat; he recognizes that his father's ruthless, survival-driven worldview shaped him, even as its influence weighs on him.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan and is Sima Gong's son and heir; his father's ruthless treatment of family shaped his rise and remains a source of inner constraint. He joined the Fire Dragon Pavilion intending to use Jin Taekyung, and Sima Gong has now ordered him to spy on Taekyung's group. Taekyung rejects defining him by his unorthodox affiliation, and Sama Pyo admires Taekyung. He was Ju Hwaran's former fiancé in a political engagement and is openly hostile toward fellow member Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1026
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet outwardly gentle; he calmly accepts sacrificing the rear population as the cost of a strategy he believes offers the best odds of victory.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1022
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 998
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃1031화



할 수 있을까, 라는 생각은 하지 않았다.

해내야 한다. 해내야 했다.

힘에는 책임이 따르고 그 막중한 책임의 무게는 뒷걸음질 칠 수조차 없게 만들었다.

그것이, 지금 이 순간 내가 나아가는 이유였다.

쉭.

아직도 손에 붙잡혀 있던 일노를 내려놓는 동시에 지면을 밟았다. 동시에 쏘아졌다.

유령환살보(幽靈幻殺步).

고금제일의 살수에게서 얻은 묘리(妙理)가 발끝에 실린다.

두 다리는 더없이 가벼웠고, 나를 스쳐 간 바람은 이내 누군가로부터 흘러나온 열기에 흔적도 없이 사라졌다.

그리고 힘주어 창대를 그러쥔 그 순간.

솨아악.

세상이 느려졌다.

머리 위 허공으로부터 벼락처럼 떨어져 내리는 일곱 줄기의 강기를 향해, 나와 적천강은 동시에 두 손을 흩뿌렸다.

콰아아아앙!

하늘이 쪼개지는 듯한 굉음과 함께, 잠시 멈췄던 시간의 흐름이 급류가 되어 터져 나왔다.

콰드드드득!

격돌의 여파로 땅거죽이 뒤집힌다. 조금 전까지만 하더라도 공기처럼 가볍던 발끝은, 언제 그랬냐는 듯이 수만 근의 중압감을 감당하지 못하고 밀려나고 있었다.

‘빌어먹을.’

격돌과 동시에 느껴지는 힘의 격차에, 나도 모르게 이가 악물렸다.

어느 정도 예상은 했지만, 그 이상이다.

일곱.

하나도, 둘도, 셋도 아닌 무려 일곱 기의 데스 나이트.

아니, 과거의 힘을 고스란히 간직하다 못해 그 이상으로 거듭난 흑의인들은 너무나도 강했다.

적천강과 함께임에도 그 위력을 감당할 수 없을 만큼.

“흡……!”

바로 옆에서 들려오는 억눌린 숨소리.

화왕(火王)이라는 별호를 증명하듯 홀로 넷이나 되는 적을 막아선 적천강이었지만, 이 찰나의 대치는 순식간에 깨져 나갈 유리병과 같았다.

바로 지금처럼.

쐐애액, 콰앙!

칠흑 같은 강기로 뒤덮인 세 자루의 창검과 백염의 창날이 다시 한번 맞닿은 순간, 나는 숨이 턱 막히는 듯한 충격과 함께 저절로 굽혀지는 무릎을 느꼈다.

‘강하다. 천산삼노 따위는 비교도 되지 않을 만큼.’

물론 천산삼노 역시 강자라 불리기에 손색이 없는 고수들이지만, 내가 단신으로 놈들을 쓰러트릴 수 있었던 것은 벽력도왕의 공력을 이어받으며 얻은 깨달음 때문만은 아니었다.

때로는 한 마리의 호랑이보다, 무리 지은 늑대들이 무서울 때가 있는 법.

천산삼노가 지금껏 쌓아 올린 악명은, 바로 후자와 같은 부분에서 기인하는 것이었다.

과거 서천마군을 따라 사천을 피로 물들였던 기련삼괴(祁連三怪)가 그러했듯이.

하지만 지금 이 순간에도 엄청난 힘과 기세로 나를 조여 오고 있는 흑의인들은 달랐다.

저들은 호랑이다.

천산삼노와는 달리 하나하나가 산맥을 호령할 수 있는, 아니 분명 과거에는 그러했을 강자들.

그리고 가장 큰 문제는 그 호랑이들이 영혼을 잃고 더욱 강해진 채, 무리를 지어 한 사람의 명령을 따르고 있다는 사실이었다.

“직접 겪어 보니 어때, 실로 대단하지 않나? 나는 저들을 흑귀(黑鬼)라고 부른다네.”

선봉의 흑의인들, 아니 일곱 명의 흑귀를 뒤따라 시시각각 가까워지는 적들의 거대한 함성 속에서도, 혈검마군의 음성은 선명했다.

한 걸음, 한 걸음 천천히 내딛는 발걸음과 함께 강렬함을 더해가는 그 기세 또한 마찬가지였다.

“그러니 너무 발악하지 말게. 적 선배야 안타까워도 어쩔 수 없다지만, 자네는 아주 중요한 전리품이거든.”

비록 흑귀들의 모습에 가려져 얼굴은 보이지 않았지만, 흐릿하게나마 눈앞에 그려졌다.

빙긋 웃고 있는 혈검마군의 얼굴이. 곧 벌어질 시산혈해(屍山血海)의 참극을 기대하며 흥분에 가득 차 있을 놈의 눈빛이.

“혹시 아나? 지금이라도 얌전히 투항한다면, 스승과 제자 둘 다 살아남을 수 있을지.”

그극. 그그극!

막강한 압력 속, 나는 간신히 목소리를 쥐어 짜냈다.

“좆…… 까!”

콰앙!

일순간 쳐 올린 창대와 함께, 세 자루의 창검이 동시에 허공으로 들렸다.

무려 사 갑자에 달하는 공력과 인간의 한계를 아득히 벗어난 신체 능력은, 영혼의 대가로 더욱 거대한 힘을 얻은 흑귀들의 합공도 잠시나마 뿌리칠 수 있게 만들었다.

그리고 그 잠깐의 빈틈은, 곧 다시 없을 기회이기도 했다.

서걱!

전력을 다해 휘두른 일격이 놈들을 베었다.

정확히는 세 마리의 커다란 흑마를, 그 자체로도 강력한 괴물이라 할 수 있는 유령마(幽靈馬)를 반으로 갈랐다.

푸화아악!

살아 있는 생물체라면 당연히 지니고 있어야 할 핏물 대신, 거무스름한 안개가 터져 나오는 믿지 못할 광경에 간신히 버티고 있던 적천강이 입을 딱 벌렸다.

“이 무슨 개 같은……!”

자세히 설명해 주고 싶지만, 지금은 때가 아니다.

순식간에 애마를 잃은 흑귀들이 잠시 균형을 잃은 틈을 타, 나는 적천강과 대치하고 있던 흑귀 넷을 향해 달려들었다.

쉬쉭 카카카캉!

베고, 찌르고, 후려치고.

그리고 벼락과도 같은 세 번의 공격을 어렵지 않게 막아 낸 놈들을 기다리고 있던 것은, 새하얀 광염에 휩싸인 적천강의 일장이었다.

“뒈져라.”

후욱, 퍼어엉!

파공성마저 지우며 쏘아진 화염신장이 한 흑귀를 후려쳤다.

정확히 가슴을 격중당한 놈이 포탄처럼 튕겨 나가는 광경에, 적천강이 이빨을 드러내며 웃었다.

아니, 정확히는 그러려고 했다.

“좋아. 이제 한 놈…….”

- 그으으.

분명 전신이 검게 그을린 채 절명했어야 할 흑귀가, 기이한 신음과 함께 신형을 바로잡기 전까지는.

“……이 아니로군.”

그래도 화염신장의 충격이 남아 있는 듯, 비틀비틀 일어나는 흑귀를 멍하니 바라보던 적천강이 나를 향해 눈을 깜빡였다.

“저 씨부럴 것들은 도대체 뭐냐?”

콰앙!

흑귀 중 하나의 검을 받아친 나는 호흡을 내뱉으며 입을 열었다.

“데스. 데스 나이트요.”

“대수대수나이두(大手大手挪移頭)라니, 그게 무슨 개같은 소리더냐.”

안타깝게도, 나는 적천강의 의문을 해소시켜 줄 수 없었다.

내가 미처 뭐라 말하기도 전에, 앞서 나가떨어진 놈까지 합류한 흑귀 전원이 동시에 달려들었으니까.

꽈아아앙!

귀가 먹먹하다. 손목에서 격통이 전해지고, 두 다리는 지면 깊숙이 박혔다.

마치 태산(太山)이 짓누르는 듯한 무시무시한 압력.

그리고 나와 적천강이 강철의 숲에 갇힌 그때, 어디선가 맹렬한 파공성이 울려 퍼졌다.

쉭, 차차창!

흑귀 중 하나가 휘두른 대도에 십여 개의 비수가 튕겨 나가는 광경에, 나는 이 싸움에 겁 없이 끼어든 누군가의 정체를 짐작할 수 있었다.

‘사마표. 이 멍청한 놈이 여기가 어디라고.’

그러나 용기와 멍청함은 한 끗 차이다.

사마표는 멍청했지만 용감했고, 고작 한 놈의 주의를 돌렸을 뿐이지만 그것만으로도 조금이나마 우리의 숨통이 트였다.

“노야, 지금!”

“염병할!”

욕설을 토해 낸 적천강이 벼락처럼 일권을 뻗었다.

콰드득!

멸염신권(滅炎神拳).

폭발하듯 터져 나온 불길이 흑빛 강기로 뒤덮인 병장기들을 잠시나마 밀어 낸다.

그리고 반경 수십여 장을 떨어 울리는 그 경천동지(驚天動地)할 위력은, 불길 사이를 쾌속하게 가로지른 섬광의 존재감을 잠시나마 가려 주기에 충분했다.

쐐애액, 푹!

사마표의 손을 떠나, 어느 흑귀의 목줄기에 틀어박힌 비수가 부르르 떨렸다.

물론, 그마저도 놈을 쓰러트리기에는 역부족이라는 사실을 나는 누구보다 잘 알고 있었다.

푸슉.

아무렇지 않게 비수를 뽑아내는 흑귀의 모습에, 잠시 포위망이 흩어진 틈을 타 뒤로 훌쩍 물러난 내가 입을 열었다.

“아까 물어보셨죠. 그래서 데스 나이트라는 게 정확히 뭐냐고.”

“…….”

“저런 새끼들입니다.”

“……니미럴. 아주 지랄났군.”

탄식하는 적천강과 달리, 곁으로 다가온 사마표의 얼굴은 침착했다.

“괴물들이로군.”

“미친놈. 아까 뒤로 빠졌어야지, 뭐 좋은 구경하겠다고 여기까지 와?”

“그렇지 않아도 후회 중이다. 그나저나 저것들은 도대체 뭐지? 일종의 강시인가?”

“비슷하긴 한데, 그것보다 좀 더 질이 안 좋은 거라고 해 두지.”

차라리 강시인 것이 천배쯤 낫다.

모산파 특산품이면 이쪽 세상 사람들의 입장에서는 적어도 토종이라 할 수 있으니까.

하지만 흑귀라 불리는 저 데스 나이트들은 외래종이다.

생태계를 파괴하고, 모든 법칙과 상식을 송두리째 무너트릴.

아니, 이미 무너트려 버린.

‘도대체 어떻게…….’

나는 조용히 침음성을 삼켰다.

어찌 이런 일이 가능한 것인지는 더는 중요하지 않았다.

이미 모두가 믿고 있던 규칙은 허물어졌고, 우리는 그 잔해를 수습해야 하니까.

그래. 비단 몇몇의 개인이 아닌, ‘우리’가.

드드득.

지면이 잘게 몸을 떨었다. 온 사방을 뒤흔들던 함성은 어느덧 내 뒤에, 적천강과 사마표의 곁에 다가와 있었다.

“무량수불.”

나직한 음성과 함께 다가온 것은 풍운검군이다.

그의 좌우에는 같은 스승 아래 동문수학한 노호검객과 태을무정검, 일천에 달하는 종남파 제자들이 있었다.

그리고 한껏 굳은 얼굴을 한 누군가 역시도.

“결국 이리되는군.”

흑야왕 사마공.

머릿수만큼은 결코 적들에 비해 떨어지지 않는, 무수한 감숙 무림인들을 거느린 그가 착 가라앉은 눈빛으로 우리를 응시한다.

아니, 정확히는 사마표를.

하지만 뭐라 말하려는 듯이 입술을 달싹였던 그는 끝끝내 아무 말 없이 입을 다물었고, 이내 정면을 응시했다.

마침내 이 드넓은 설원(雪原)에서 맞닥트린, 사막 너머의 지배자들을.

“그만.”

묵묵히 우리를 향해 다가오던 흑귀들이 동시에 걸음을 멈췄다. 그 중심으로 수만여 명의 대군을 등진 혈검마군이 걸음을 내디뎠다.

저벅.

“그래, 이렇게 나와 줘야지.”

우우웅.

별호와는 어울리지 않는, 그러나 정마대전을 장식한 무수한 마두 중에서도 손꼽히는 혈겁(血劫)을 쌓았던 회백색 검신이 몸을 떨었다.

검붉은 강기를 울컥울컥 쏟아내며, 끊임없이 잇고 결합시키며 정면을 향해 겨누어졌다.

돌아가기에는 모든 것이 늦어 버린, 그렇기에 온 힘을 다해 나아갈 수밖에 없는 방해꾼들을 향해.

으아아아아!

함성이, 살기가, 두려움과 분노가 뒤섞이고 증폭된다.

그 격렬한 감정의 소용돌이 속, 나는 천천히 걸음을 떼었다.

사박.

차갑다. 발끝에서 서리가 부서진다.

두근.

심장이 뛴다.

가파르고 거친 그 박동에 맞춰, 발걸음의 속도를 높였다.

쉭. 쐐애애액!

바람이 불었다. 선선했던 산들바람이 광풍(光風)이 되어 휘몰아치고, 나는 광풍을 불러일으켰다.

아니, 이 거대한 전장의 모두가.

와아아아아!

함성과 구름, 바람.

그 너머에서 번뜩이는 수많은 날붙이들.

그리고 눈부시도록 새하얀 설원을 가로지른 두 갈래의 거대한 군세가, 마침내 그 중심에서 격돌했다.

콰드드드득!

새하얀 눈밭이 붉게 물든다.

뭉클거리며 번져 가는 피 안개 속, 그 무수한 비명과 죽음을 비집고 초인(超人)들은 서로를 향해 쏘아졌다.
```

## Final English reading copy

```markdown
# Chapter 1031

I didn’t wonder if I could do it.

I had to. I had to see it through.

Power came with responsibility, and the weight of that responsibility left no room to retreat.

That was why I was moving forward now.

Whoosh.

I lowered the First Elder, still in my grip, and planted my foot on the ground. In the same instant, I shot forward.

Ghost Illusory Slaughter Step.

The subtle art I’d learned from the greatest assassin of all time flowed through my feet.

My legs felt impossibly light. The wind brushed past me, then vanished without a trace in the heat radiating from someone nearby.

And the moment I tightened my grip on the shaft—

Swaaash!

The world slowed.

As seven streams of Force fell like lightning from the sky above, Jeok Cheongang and I flung out our hands at the same time.

KWA-BOOOOM!

With a deafening crash that seemed to split the sky, time—which had paused for a moment—burst forth like a raging torrent.

KRRRUNCH!

The ground flipped over from the force of the collision. My feet, light as air only moments ago, were driven back under a pressure of tens of thousands of pounds.

*Damn it.*

The instant our forces collided, I felt the difference in strength and clenched my teeth before I could stop myself.

I’d expected them to be strong, but this was beyond that.

Seven.

Not one, not two, not three—but seven Death Knights.

No, the men in black were far too powerful. They hadn’t merely kept all their former strength; they’d grown stronger still.

Their power was too much to withstand, even with Jeok Cheongang at my side.

“Hngh…!”

A muffled breath came from right beside me.

Jeok Cheongang was holding off four enemies alone, proving his title as the Fire King. But this momentary standoff was like a glass bottle on the verge of shattering.

Just as it was now.

SHWING! KRAANG!

The three spears and swords, shrouded in pitch-black Force, met the White Flame’s blade once more. The impact left me gasping, and I felt my knees bend on their own.

*They’re strong. The Three Elders of Tianshan don’t even compare.*

The Three Elders were certainly masters worthy of being called powerful. But my ability to defeat them alone hadn’t come from inheriting the Thunderbolt Saber King’s internal energy and gaining insight alone.

Sometimes a pack of wolves is more frightening than a single tiger.

The Three Elders’ infamy, built over all these years, came from the same reason as the wolves’.

Just like the Qilian Three Fiends, who had once followed the Western Heaven Demon Lord and drenched Sichuan in blood.

But the men in black, closing in on me with tremendous strength and momentum even now, were different.

They were tigers.

Unlike the Three Elders of Tianshan, each one could command an entire mountain range—or, at least, they must have been able to in the past.

And the worst part was that these tigers had lost their souls, grown even stronger, and were now moving as a pack at the command of one man.

“How do they seem, now that you’ve faced them yourself? Impressive, aren’t they? I call them Black Ghosts.”

Even with the enemy’s enormous roar drawing ever closer behind the vanguard of men in black—the seven Black Ghosts—the Blood-Sword Demon Lord’s voice rang clear.

So did his aura, growing more intense with each slow step.

“Don’t struggle too hard. I regret what must happen to Senior Jeok, but you’re a very important prize.”

I couldn’t see his face behind the Black Ghosts, but I could picture it, if only faintly.

The Blood-Sword Demon Lord smiling. His eyes shining with excitement at the sea of corpses and blood about to unfold.

“Who knows? If you surrender peacefully now, perhaps both master and Disciple can survive.”

Grrk. Grrrk!

Under the crushing pressure, I barely managed to force out my voice.

“Fuck… off!”

KWAANG!

I thrust the spear shaft upward. All three of their spears and swords flew into the air at once.

As much as four jiazi of internal energy and a body far beyond human limits let me repel the Black Ghosts’ combined attack, strengthened at the cost of their souls, if only for a moment.

And that brief opening was a chance that wouldn’t come again.

SHHK!

I swung with all my strength and cut them down.

More precisely, I cut three huge black horses in half—ghost horses, monsters powerful enough to be considered terrifying in their own right.

FWOOOSH!

Instead of the blood any living creature should have had, a dark mist burst out. Jeok Cheongang, who’d been barely holding on, gaped at the unbelievable sight.

“What kind of fucked-up—!”

I’d love to explain, but now wasn’t the time.

Taking advantage of the Black Ghosts’ brief loss of balance after suddenly losing their steeds, I charged the four who’d been facing Jeok Cheongang.

SHK-SHK! KAKAKANG!

I slashed, stabbed, and swung.

The men blocked all three lightning-fast attacks without difficulty. Waiting for them was Jeok Cheongang’s palm strike, wreathed in brilliant white flames.

“Die.”

Whoosh—BOOM!

The Flame Divine Palm shot forward, erasing even the sound of its passage. It struck one of the Black Ghosts.

The man took the blow square in the chest and flew back like a cannonball. Jeok Cheongang bared his teeth in a grin.

Or, at least, he tried to.

“Good. That’s one—”

—Grrr.

But then the Black Ghost, who should have died with his whole body scorched black, let out a strange groan and straightened up.

“…No, it isn’t.”

Perhaps the Flame Divine Palm’s force still lingered. Jeok Cheongang stared blankly as the Black Ghost staggered to his feet, then blinked at me.

“What the hell are those things?”

KWAANG!

I parried the sword of one of the Black Ghosts and let out a breath before answering.

“Death. Death Knights.”

“Great Hand, Great Hand, Shift-Head? What the hell are you talking about?”

Unfortunately, I couldn’t clear up Jeok Cheongang’s confusion.

Before I could say anything, every Black Ghost—including the one who’d just been knocked away—charged at once.

KWA-BOOOOM!

My ears rang. Pain shot through my wrist, and both my legs sank deep into the ground.

A terrifying pressure, as if Taishan itself were bearing down on me.

And just as Jeok Cheongang and I were trapped in a forest of steel, a fierce rush of air sounded from somewhere.

Whoosh—CLANG-CLANG!

A large saber swung by one of the Black Ghosts knocked away a dozen or so throwing knives. I could guess who had fearlessly jumped into this fight.

*Sama Pyo. You idiot. What the hell are you doing here?*

But there was only a hair’s breadth between courage and stupidity.

Sama Pyo was an idiot, but he was brave. He’d only distracted one of them, but even that gave us a little room to breathe.

“Old Master, now!”

“Damn it!”

Jeok Cheongang spat a curse and shot out his fist like lightning.

KRRRUNCH!

Flame-Extinguishing Divine Fist.

Flames erupted like an explosion, pushing back the weapons wrapped in black Force, if only for a moment.

Its earth-shaking power reached hundreds of feet in every direction. It was enough to hide, for a moment, the streak of light racing through the flames.

SHWING! THUNK!

A throwing knife had left Sama Pyo’s hand and sunk into one Black Ghost’s throat. The blade quivered.

Of course, I knew better than anyone that even that wouldn’t be enough to bring him down.

Pshk.

The Black Ghost pulled the knife out as if it were nothing. Taking advantage of the brief gap in the encirclement, I leaped back and spoke.

“You asked earlier, didn’t you? What exactly a Death Knight is.”

“……”

“They’re bastards like that.”

“……Shit. This is a fine mess.”

Jeok Cheongang sighed. Sama Pyo, who’d come up beside us, remained calm.

“What monsters.”

“Idiot. You should’ve fallen back earlier. What, did you come all this way for a good view?”

“I already regret it. But what exactly are they? Some kind of jiangshi?”

“Similar, but let’s say they’re a bit worse.”

Jiangshi would be a thousand times better.

If they were a Maoshan Sect specialty, then at least from the point of view of people in this world, they’d be native creatures.

But those Black Ghosts—the Death Knights—were an invasive species.

They would destroy the ecosystem and shatter every law and bit of common sense.

No—they already had.

*How could this happen…?*

I swallowed back a quiet groan.

How such a thing was possible no longer mattered.

The rules everyone had believed in had already crumbled, and we had to deal with the rubble.

That’s right. Not just a handful of individuals. *We* did.

Rumble, rumble.

The ground trembled. The roar that had shaken everything around us was now behind me, beside Jeok Cheongang and Sama Pyo.

“Infinite Life Buddha.”

The one approaching with a low invocation was the Wind-and-Cloud Sword Lord.

At his sides were the Roaring Fury Swordsman and the Taeeul Merciless Sword, fellow disciples under the same master, along with nearly a thousand disciples of the Zhongnan Sect.

And another man, his face set hard.

“So it comes to this.”

The Black Night King, Sima Gong.

With countless martial artists from Gansu at his command, his numbers were in no way inferior to the enemy’s. His eyes were fixed on us, cold and sunken.

No—more precisely, they were fixed on Sama Pyo.

His lips moved as though he wanted to say something, but in the end he shut his mouth without a word and looked straight ahead.

He looked straight at the rulers from beyond the desert, whom we had finally met on this vast snowy plain.

“Enough.”

The Black Ghosts, who’d been silently advancing toward us, all stopped at once. The Blood-Sword Demon Lord stepped forward, with an army of tens of thousands behind him.

Thud.

“Good. This is how you should meet me.”

Vrrrrm.

The gray-white blade trembled. Its color hardly suited the Blood-Sword Demon Lord’s title, though it had reaped carnage that ranked among the worst of the Great Faction War.

Dark-red Force surged from the blade, linking and binding together without pause as he leveled it at the men in his way—men who could no longer turn back and had no choice but to press forward with all their strength.

Aaaaaah!

Shouts and killing intent, fear and anger—all mixed together and swelled.

In the midst of that violent whirlpool of emotion, I took a slow step forward.

Crunch.

Cold. Frost broke beneath my toes.

Thump.

My heart pounded.

With each harsh, pounding beat, I quickened my pace.

Whoosh. SHWAAAAA!

The wind blew. The mild breeze became a raging gale, and I summoned that gale.

No—the whole battlefield did.

WAAAAAH!

Shouts, clouds, wind.

Beyond them, countless blades flashed.

And two vast armies raced across the dazzling white snowfield, colliding at last in its center.

KRRRUNCH!

The white snow turned red.

In the blood mist, swelling and spreading, superhumans shot toward one another, cutting through countless screams and deaths.
```
