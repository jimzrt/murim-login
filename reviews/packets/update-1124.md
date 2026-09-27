<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1124.txt",
      "sha256": "e396b3377aa57f50cdddcdbdf68a5d04fd43ad14c0047ac37db4f83ec2d87615",
      "bytes": 12068
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "67ffe08cc2a906e07b251e08025ab50dc30d83382d7c296f71845d64dd683e4d",
      "bytes": 1038
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "307189767337c5394589bdcaa7f59f3e28cdf1da9d380fecae4d63447025be4b",
      "bytes": 245178
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "3dea10809f41ca8d97fdfaf7076ad563d7dd8100a5d9094f69b2bdee1ed12947",
      "bytes": 944
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "37f58e67f198944b0801e2b635b823ff2a75ae567d7b058fe29fd26a73f50f64",
      "bytes": 1230
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0d09693ffa511b9e7df91dcc1c96a6dc9006456f4b412811aede5305759cbc4b",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "8c651d8d91fe30cb16efecef4376eb8ff3e84d2ca54207352e7a4c7360a3b401",
      "bytes": 1513
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "3bea3f370c029761f58251ee13c007ec09263b5bbc337a50cca97ff50392f1ed",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "ebabe898af84bc40d35ad5952c350e5c19b4d03b6256fa73f68acd12676dee47",
      "bytes": 623
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "0ed94d23f9d01994ce9f84e470c2e838c7fa3033760282fc3f3168423ee428f0",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fbe26e0ec5f89ce57df0b052ec3ff3869882eaa7728f4db5939e2d5122fb744c",
      "bytes": 289919
    }
  ],
  "estimated_tokens": 10663
}
-->

# Durable State Update — Chapter 1124

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
1 and safe_through 1124. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1124. Profile updates may replace only one
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
  "chapter": 1124,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1124,
    "continuity_sources": [1124],
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
    "The Inner City remains under siege; defenders and civilians are fighting to protect Taekyung.",
    "Taekyung is critically injured but fighting under Final Rally; the quest timer has five minutes remaining.",
    "Jeok Cheongang and Cheongpung are advancing with Taekyung toward the Blood Lord.",
    "The Slaughter Saint and Bow Saint are engaging two magically enhanced, regenerating Black Ghosts.",
    "Taekyung believes Hyuk Mujin is dead, though he did not witness his fate.",
    "Taekyung remembers an unfulfilled promise to Ju Hwaran."
  ],
  "continuity_sources": [
    1123
  ],
  "open_questions": [
    "Will Taekyung survive the remaining quest time and reach the Blood Lord?",
    "Can the Saints defeat the regenerating Black Ghosts?",
    "What happened to Hyuk Mujin?",
    "Will Taekyung ever fulfill his promise to Ju Hwaran?"
  ],
  "safe_through": 1123,
  "temporary_decisions": [
    "Render 부각주 as “Vice Captain” when Taishan addresses Hyuk Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 삼성     | **Three Saints**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 화산     | **Huashan**            |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 숭산 | **Mount Song** | Mountain where Shaolin Temple is located. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 매화삼십육검 | **Thirty-Six Plum Blossom Swords** | Huashan sword technique used by Cheongpung. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 화산신룡 | **Huashan Divine Dragon** | Title given to Cheongpung after the Star-Array Grand Banquet. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 수강 | **Palm Force** | Force generated through a palm technique. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 지옥도 | **hellscape** | Metaphorical description of the devastated battlefield. |
| 적도 | **Red Blade** | Named blade that shatters in Taekyung’s flames. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 진태경 | 혈주 | hostile_opponent_to_hostile_opponent | you; you son of a bitch | insulting-casual | Taekyung insults the Blood Lord while challenging his claim that he will kill him. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1123
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure and formidable combatant who commands weapons telekinetically and absorbs blood to restore vitality; after killing the Grand Mage, he claims command of the Dark Heaven army.
- **Personality:** Cunning and controlling, he plans around opponents’ strengths and trusts his overwhelming power; his newly unrestrained madness leads him to defy the Lord of Heaven’s will and seize command for himself.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He has served the Lord of Heaven but now openly defies his will; he is fixated on killing Jin Taekyung, killed the Grand Mage, and recognizes Cheongpung from his connection to Sword Saint Mae Jonghak.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1123
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has mastered the Slaughter Saint’s Ghost Illusory Slaughter Step and blended it with his Dark Fragrance Drift.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, and compassion; guided by his grandfather’s righteousness and Taekyung’s chivalry, he meets danger with resolve and trusts Taekyung without wavering.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint is his mentor in concealment and Ghost Illusory Slaughter Step.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1123
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1123
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1122
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1122
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1123
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1124화



삐빅.



제한 시간 : 5분 00초



이 광활한 전장에서 오직 한 사람에게만 허락된 시계의 초침이 움직인 그 순간.

팟.

공간이 갈라졌다.

지워지고, 부서졌다.

그리고 그 중심에, 전력을 다하여 서로를 향해 쏘아지는 네 개의 신형이 있었다.

정확히는, 한 마리의 괴물과 그에 맞서는 세 명의 인간이.

바로 그, 진태경이.

솨악!

소름 끼치도록 낮은 파공성이 귓가를 파고든다.

소리마저 앞지른, 태산을 쪼개지는 듯한 일격.

비스듬히 내리그어진 적도(赤刀)는 그만큼 쾌속하면서도 강맹했다.

진태경 자신이 평소와 같은 상태였더라도 저 움직임을 제대로 볼 수 있었을까, 하는 의문이 들 정도로.

설령 보았다 하더라도, 도신을 휘감은 거대한 강기를 맞받아칠 엄두조차 내지 못했을 정도로.

하지만 죽음의 끝자락에서 그 어느 때보다 날카롭게 벼려진 감각은, 아직 식지 않은 진태경의 육신을 생로(生路)로 이끌고 있었다.

스륵.

바람이 멎는다, 시간이 느려진다.

먹구름이 낀 하늘처럼 흐릿한 진태경의 동공에, 아슬아슬하게 코앞을 스쳐 지나가는 핏빛 도신과 타오르는 강기가 비쳤다.

서걱!

한 뼘 차이로 빗나간 궤적을 따라, 마치 두부처럼 갈라지는 지면.

그와 함께 칼날처럼 휘몰아친 풍압(風壓)이 몸을 할퀴었으나, 이미 고통을 잊은 진태경은 홀린 듯이 창을 내뻗었다.

슈확!

공간을 정확히 관통하는 창날.

그와 동시에 적천강의 멸염신권(滅炎神拳)이, 청풍의 검이 바람을 갈랐다.

화륵, 쉬쉬쉬쉭!

두 줄기의 불꽃이 한 몸처럼 뒤섞여 나아가고, 노을을 닮은 자줏빛 강기가 꽃잎이 되어 흩날린다.

비록 정도의 차이는 있을지언정, 각각의 명성만으로도 천하 무림을 떨어 울리는 세 초절정 고수의 완벽한 합공(合攻).

하지만 그런 그들을 기다리고 있는 존재는, 이미 인간의 한계를 아득히 뛰어넘은 괴물이었다.

화아악.

일순간 들끓어 오르는 거대한 기운.

그와 동시에 어느덧 칼자루에서 떨어져 나온 혈주(血主)의 양손이, 한 줄기의 벼락처럼 공간을 후려쳤다.

퍼어어엉!

소리마저 앞지른 쌍장(雙掌).

하늘이 쪼개지는 듯한 굉음과 함께, 혈주를 중심으로 터져 나온 핏빛 섬광이 사방을 휩쓸었다.

적과 아군조차 구분하지 않는, 압도적이면서도 파괴적인 힘으로.

구구구궁……!

깊은 울림이 초토화된 공간을 휘감으며 뻗어 나갔다.

삽시간에 무수한 육편(肉片)이 되어 흩어진 광신도들의 시체를 넘어, 비틀거리며 신형을 바로 세우는 세 사람에게까지.

“이걸 살아?”

혈주는 자신도 모르게 중얼거렸다.

그만큼 전력을 다한 일격이었으니까.

단 한 번의 공격으로 지닌 힘의 삼분지 일을 쏟아부었을 만큼.

반경 십여 장에 존재하는 모든 생명체를 지우고, 죽음만이 내려앉은 지옥도(地獄道)로 변모시킬 만큼.

물론 전혀 예상하지 못했던 상황은 아니었다.

제아무리 심각한 상처를 입고 피를 흘린다 해도, 결국 맹수는 맹수.

저들 중 가장 나약한 맹수조차, 화산신룡(華山神龍)이라 불린다는 것을 생각한다면 더더욱 그랬다.

아니, 오히려 잘 된 것일지도 모른다.

조금 전의 일격으로 모조리 죽여 버렸다면, 되려 그 자신이 허무해졌을지도 모를 테니까.

“안 되지. 이렇게 쉽게는.”

낮게 깔린 웃음소리와 함께, 혈주가 걸음을 뗀 그 순간이었다.

스륵.

불현듯 느껴지는 이질감.

동시에 손바닥을 들어 그 이질감의 정체를 확인한 혈주의 눈빛이 착 가라앉았다.

피다.

상처라고 부르기조차 민망한, 얕게 벌어진 살갗 틈새로 몽글몽글 솟아오른 핏방울이 손바닥 위로 흐르고 있었다.

조금 전 누군가의 공격을 정면에서 맞받아쳤던, 바로 그 손으로부터.

“이건…….”

문득 말꼬리를 흐린 혈주는 천천히 고개를 들었다.

동시에, 보았다.

머리부터 발끝까지 피로 뒤덮인 채, 가쁘게 호흡을 가다듬고 있는 한 사람을.

지금 당장이라도 쓰러져도 이상하지 않을 만큼 창백한 그의 얼굴과 아직 사그라지지 않은 불꽃이 담겨 있는 두 눈동자를.

‘진태경.’

혈주는 붉은 혀를 내밀어 입술을 핥았다.

어찌 된 일일까.

분명 막았다고 생각했는데.

저들 중 그 누구의 공격도, 자신의 양손에 깃든 수강(手罡)을 깨트릴 수 없었을 텐데.

하지만.

“그래, 이래야지. 응당 이 정도는 해 주어야지.”

혈주는 혼잣말처럼 낮게 속삭였다.

가라앉았던 눈빛이 형형하게 살아나고, 흔들리던 입꼬리는 부드럽게 올라갔다.

지금 이 순간, 그는 진심으로 즐거워하고 있었다.

방심? 혹시 모를 상황에 대한 두려움?

그런 것 따위는 처음부터 없었다.

그저, 확신할 뿐이었다.

눈앞의 사냥감이 힘없는 토끼건, 혹은 이빨을 숨기고 있는 맹수건 반드시 사냥할 수 있다는 확신.

단 일합(一合)의 공방이었으나, 혈주는 새삼 다시 한번 깨달을 수 있었다.

지금 이 순간 자신에게 깃든 힘이 얼마나 거대한지.

동시에, 얼마나 무한한지.

철퍽.

나아가는 괴물의 발걸음을 따라, 작은 호수처럼 고인 피 웅덩이가 휘몰아치듯 빨려 들어갔다.

솨아아아악!

탐욕스럽게 핏물을 집어삼킨 혈주가, 재차 차오르는 힘에 도취 된 괴물이 섬광처럼 공간을 가로질렀다.

투둑.

뒤늦게 떨어진 한 방울의 피를 남긴 채.



* * *



혈주의 확신은 결코 오만이 아니었다.

재차 쏘아지는 그의 움직임은 전장의 그 누구보다 쾌속했고, 적도를 타고 터져 나오는 거대한 핏빛 강기는 보는 이로 하여금 미증유(未曾有)라는 세 글자를 떠올리기에 충분했으니까.

적어도 지금 이 순간.

그는 이 광활한 전장에서 가장 강력한 포식자이자, 누구도 대적할 수 없는 절대자였다.

삼성(三星)에 속한 두 거인마저 적들의 거센 반격에 발이 묶인 이상, 이미 저마다 심각한 부상을 입은 세 명의 초절정 고수쯤은 단숨에 짓뭉개 버릴 수 있을 정도의.

그리고 그 사실을 누구보다 잘 알고 있기에, 진태경은 지금의 이 상황을 이해할 수 없었다.

쐐애애액!

도대체 어째서.

콰드드득!

태산을 쪼개고도 남을 것만 같은 저 무시무시한 강기가.

슈확!

바람보다도, 소리와 빛마저도 앞지를 것 같은 혈주의 움직임이.

후우우웅!

매번, 매 순간 자신을 아슬아슬하게 스쳐 지나가는지.

닿지 않는지.

“네놈……!”

칼날처럼 휘몰아치는 바람 속, 메아리치듯 울려 퍼지는 괴물의 음성을 진태경은 듣고 있지 않았다.

아니, 정확히는 듣지 못했다.

쉴 새 없이 흐릿한 시야를 물들이는 섬광 속에서, 무언가에 홀린 듯 움직임을 이어 나갈 뿐.

서걱!

나아가려던 발걸음을 제자리로 되돌리고, 고개를 숙임과 동시에 핏빛 강기가 머리 위를 스친다.

단 한 치의 망설임도 없는, 완벽에 가까운 회피.

저토록 빠르고 강맹한 일격을 어떻게 피할 수 있었는지, 또 왜 이런 선택을 했는지에 대한 이유는 진태경 자신조차 몰랐다.

그저, 그래야만 할 것만 같았다.

이 모든 것이 당연하게 느껴졌다.

매일 아침 동쪽에서 떠오르는 태양과, 위에서 아래로 흐르는 물처럼.

마치 미리 정교하게 합을 짜 맞춘 비무처럼.

그러나 그것은 오직 진태경 한 사람에게만 해당하는 이야기일 뿐이었다.

스륵, 쐐애애액!

진태경의 정수리를 향해 내리그어지던 적도가 돌연 방향을 뒤튼 그 순간.

콰앙!

한 줄기의 굉음과 함께, 사각을 노리고 달려들던 청풍이 울컥 피를 토해 내며 무릎을 꿇었다.

그의 머리 위에서는 매화삼십육검(梅花三十六劍)의 검로를 단숨에 지워 내며 벼락처럼 떨어져 내린 적도가, 만근의 무게로 검신을 짓누르고 있었다.

쩌저적.

자줏빛 강기가 급격히 사그라듦과 동시에 거미줄처럼 번져 가는 실금.

핏물을 삼키며 온 힘을 끌어올리는 청풍을 향해, 혈주의 검붉은 혈광(血光)이 쏟아져 내렸다.

“감히 네깟놈이-!”

앞서 괴물이 느꼈던 즐거움은 어느덧 분노로 변해 있었다.

도대체 왜, 어째서.

이토록 강대한 무위를 갖추었음에도, 진태경은 분명 죽어 가고 있음에도 자신은 이 간단하고도 확실한 전투를 끝맺지 못하는 것일까.

그리고 이미 승패가 정해진 것이나 다름없는 상황 속에서도, 눈앞의 빌어먹을 애송이는 왜 끝까지 저항하는 것일까.

그에게 있어 낙인과도 같은 치욕을 안겨 주었던, 숭산(嵩山)에서의 그날처럼.

“그래, 네놈부터 죽여 주마.”

씹어뱉는 듯한 한 마디와 함께, 한층 크기를 부풀린 핏빛 강기가 검신을 파고든 그 순간이었다.

화아악.

불현듯 등 뒤에서 들이닥치는 뜨거운 열기에, 망설임 없이 칼자루를 놓은 혈주가 일권(一拳)을 내뻗었다.

콰아아앙!

허공에서 격돌한 두 개의 주먹.

서로를 집어삼키기 위해 달려드는 백색 광염과 핏빛 강기.

그러나 그 힘의 차이는 이미 명백했고, 혈주는 짙은 아지랑이 너머로 보이는 적천강을 향해 이빨을 드러냈다.

“꺼져라, 늙은이.”

퍼엉!

피처럼 붉은 강기가 불꽃을 집어삼켰다. 폭발음과 함께 힘없이 튕겨 나간 적천강의 신형이 지면을 나뒹굴었다.

조금 전까지만 하더라도 누군가가 있던, 바로 그 자리에.

‘……뭐?’

깨달음은 찰나였다. 

그리고 불현듯 혈주의 뇌리에 울려 퍼지는 적신호와 동시에, 한 줄기의 바람이 공간을 가로질렀다.

스아아.

소름이 끼칠 만큼, 낮고 희미한 파공성.

어느덧 느려진 시간 속에서 돌아서는 혈주의 핏빛 동공에, 흐린 눈빛으로 창을 내뻗는 진태경의 모습이 틀어박혔다.

“……!”

혈주는 어떻게, 라는 세 글자조차 내뱉지 못했다.

압도적으로 강한 자신이, 어찌하여 시시각각 죽음의 늪으로 빠져가는 저 핏덩어리의 기척을 놓쳤는지에 대해서도 생각할 수 없었다.

그리고 그것은, 진태경 역시 마찬가지였다.

‘지금이야.’

마치, 자신이 모르는 또 다른 누군가가 귓가에 속삭이는 듯했다.

희뿌옇게 물든 시야에는 아무것도 보이지 않았음에도.

줄어드는 시간과 함께 끔찍한 피로가, 그보다 더한 죽음의 기운이 육신에 스며들고 있음에도.

스악.

진태경은 부드럽게 창을 내질렀다.

지금 이 순간에도 끊임없이 울려 퍼지는 적과 아군의 함성과 비명도, 서늘한 강철의 소음과 어느덧 성큼 가까워진 나팔 소리도.

그리고 혈주가 본능적으로 내뻗은 손바닥도.

아무것도 그를 막을 수 없었다.

그 모든 것을 뒤로한 채, 그저 처음부터 정해져 있던 것처럼 일점(一點)을 향해 몸속 깊숙한 곳의 화염을 흘려보냈다.

푸욱.

미약한 열기가 실린 창날이, 강기에 휩싸인 손바닥을 관통하며 뻗어 나갔다.

어째서인지 아직까지도 상처가 치유되지 않은, 바로 그 손을 지나.

콰드드득!

터질 듯 부릅떠진 괴물의 두 눈동자를 경악으로 물들이며.
```

## Final English reading copy

```markdown
# Chapter 1124

*Beep.*

> **System**
>
> **Time Limit:** 5 minutes, 00 seconds

At the moment the second hand of the clock granted to only one person on this vast battlefield began to move—

*Flash.*

Space split apart.

It was erased, shattered.

And at its center, four figures were hurtling toward one another with all their might.

More precisely, one monster and the three humans standing against it.

And one of them was Jin Taekyung.

SHWAAK!

A horrifyingly low whistle of air pierced his ears.

A strike that split mountains, faster than sound itself.

The Red Blade came down at an angle, swift and fierce in equal measure.

Jin Taekyung wondered whether he could have properly seen that movement even in his usual condition.

Even if he had, he wouldn’t have dared to meet the enormous Force coiling around the blade head-on.

But his senses, honed sharper than ever at the edge of death, were guiding his still-warm body toward a path of survival.

*Rustle.*

The wind stopped. Time slowed.

In Jin Taekyung’s hazy pupils, like a sky clouded over, the blood-red blade and its blazing Force passed within a hair’s breadth of his face.

*Slice!*

Along the path that missed him by mere inches, the ground split as easily as tofu.

The wind pressure whipped around like a blade and tore at his body, but Jin Taekyung had already forgotten pain. As if entranced, he thrust out his spear.

SHWAAK!

The spearhead pierced straight through space.

At the same time, Jeok Cheongang’s Flame-Extinguishing Divine Fist and Cheongpung’s sword cleaved through the wind.

FWOOSH, SHWISH-SHWISH-SHWISH!

Two streams of flame surged forward as one, while violet Force, like the colors of sunset, scattered like flower petals.

Though their renown varied, each of the three Supreme Peak masters could make the entire Murim tremble on the strength of his name alone. Together, they launched a perfect combined attack.

But waiting for them was a monster that had already far surpassed the limits of humanity.

HWAASH!

An enormous energy boiled up in an instant.

At the same time, the Blood Lord’s hands—now both free of the hilt—struck through space like twin bolts of lightning.

KWA-BOOOOM!

Twin palms, faster than sound itself.

With a roar as if the sky had split, a blood-red flash erupted around the Blood Lord and swept in every direction.

An overwhelming, destructive force that made no distinction between friend and foe.

RUMBLE, RUMBLE……!

A deep reverberation surged through the devastated battlefield.

It swept over the countless fanatics’ corpses, now scattered as chunks of flesh, and reached the three men staggering back to their feet.

“They survived that?”

The Blood Lord muttered despite himself.

He had put tremendous power into that strike.

He had poured a third of his strength into a single attack.

It had been powerful enough to erase every living thing within a radius of over ten jang and turn the area into a hellscape where only death remained.

Of course, he hadn’t thought the outcome was entirely impossible.

No matter how grievously wounded and bloodied they were, a beast was still a beast.

Especially when even the weakest beast among them was called the Huashan Divine Dragon.

No—perhaps this was for the best.

If he’d killed them all with that last strike, he might have been left feeling empty.

“No. Not like this. Not so easily.”

It was just as the Blood Lord took a step forward, a low laugh escaping him.

*Rustle.*

A strange sensation came over him without warning.

He raised his hand to inspect it, and his gaze immediately turned cold.

Blood.

A bead of blood welled up through a shallow split in his skin—too slight to even call a wound—and ran across his palm.

From the very hand that had just met someone’s attack head-on.

“This is……”

The Blood Lord’s voice trailed off. Slowly, he lifted his head.

And saw him.

One man, covered in blood from head to toe, breathing hard as he steadied himself.

His face was so pale he could have collapsed at any moment, yet his eyes still held a flame that hadn’t died out.

*Jin Taekyung.*

The Blood Lord ran his red tongue over his lips.

How had this happened?

He’d been sure he had blocked the attack.

None of their strikes could have broken the Palm Force gathered in his hands.

And yet—

“Yes. This is how it should be. You ought to manage at least this much.”

The Blood Lord murmured softly, almost to himself.

The light that had dimmed in his eyes flared to life, and his wavering lips curled into a gentle smile.

At this moment, he was truly enjoying himself.

Carelessness? Fear of what might happen?

He’d felt none of that from the start.

He had simply been certain.

Certain that he could hunt the prey before him, whether it was a powerless rabbit or a beast hiding its fangs.

Though it had been only a single exchange, the Blood Lord had realized once again just how immense the power within him was at this moment.

And how boundless.

*Squelch.*

As the monster stepped forward, the pool of blood at his feet, spread out like a small lake, swirled and rushed toward him.

SHWAAAAA!

The Blood Lord greedily swallowed the blood. Intoxicated by his strength surging anew, the monster shot through space like a flash of light.

*Drip.*

A single drop of blood fell behind him.

* * *

The Blood Lord’s confidence was no arrogance.

He moved faster than anyone else on the battlefield, and the immense blood-red Force bursting from his Red Blade was enough to make anyone who saw it think of the word *unprecedented*.

At least at this moment.

He was the strongest predator on this vast battlefield, an absolute being no one could oppose.

With even the two giants among the Three Saints pinned down by the enemies’ fierce counterattack, he was powerful enough to crush the three Supreme Peak masters—each already seriously injured—in an instant.

And Jin Taekyung knew that better than anyone. Which was why he couldn’t understand what was happening.

SHWEEEE!

Why—

KRRRCH!

Why was that terrifying Force, powerful enough to split a mountain—

SHWAAK!

Why was the Blood Lord’s movement, faster than wind, sound, even light—

WHOOOOSH!

Missing him by a hair every time, every single moment?

Why couldn’t it touch him?

“You—!”

Jin Taekyung didn’t hear the monster’s voice echoing through the blade-sharp wind.

No. More precisely, he couldn’t hear it.

Amid flashes that constantly blurred his vision, he simply kept moving as if entranced.

*Slice!*

He brought his advancing foot back to where it had been, ducked his head, and let the blood-red Force pass overhead.

A flawless dodge, without a moment’s hesitation.

Jin Taekyung himself didn’t know how he could evade such a swift and ferocious strike. He didn’t know why he’d made that choice, either.

He just felt he had to.

It all seemed perfectly natural.

Like the sun rising in the east each morning, or water flowing downhill.

Like a duel whose every move had been carefully arranged in advance.

But that was true only for Jin Taekyung.

*Rustle, SHWEEEE!*

Just as the Red Blade, descending toward the crown of Jin Taekyung’s head, abruptly changed direction—

KWAANG!

With a single deafening crash, Cheongpung, who had rushed in to attack from the blind spot, dropped to one knee and spat up blood.

Above him, the Red Blade had wiped away the path of the Thirty-Six Plum Blossom Swords in an instant and crashed down like lightning, its weight pressing into his sword as if it weighed ten thousand geun.

CRACK.

The violet Force faded rapidly, and hairline fractures spread across the blade like a spiderweb.

As Cheongpung swallowed blood and summoned all his strength, the Blood Lord’s dark-red light poured down on him.

“You dare, you little—!”

The monster’s earlier delight had turned to anger.

Why? How?

With martial prowess this immense, and Jin Taekyung clearly dying, why couldn’t he finish this simple, certain fight?

And even when victory was all but decided, why did that damned brat before him keep resisting to the end?

Just as he had on that day at Mount Song, when he’d inflicted a humiliation that was like a brand upon the Blood Lord.

“Fine. I’ll kill you first.”

As the Blood Lord spat out the words, the blood-red Force swelled and surged into the blade.

Then—

HWAASH!

Feeling a wave of heat sweep in from behind him, the Blood Lord released the hilt without hesitation and thrust out a fist.

KWA-BOOOOM!

Two fists collided in midair.

White flames and blood-red Force charged at each other, each trying to devour the other.

But the difference in their power was already clear. Through the thick heat haze, the Blood Lord bared his teeth at Jeok Cheongang.

“Get lost, old man.”

*BOOM!*

Blood-red Force swallowed the flames. With an explosion, Jeok Cheongang’s body was sent flying helplessly and rolled across the ground.

Right where someone had been standing just moments before.

*…What?*

The realization came in an instant.

At the same time, an alarm rang in the Blood Lord’s mind, and a gust of wind cut through space.

*Fwoosh.*

A whistle of air so low and faint it raised goose bumps.

In time slowed to a crawl, the Blood Lord turned. Jin Taekyung’s figure was fixed in his blood-red pupils, thrusting out his spear with unfocused eyes.

“……!”

The Blood Lord couldn’t even manage to say the words *How?*

He couldn’t think about how he, overwhelmingly powerful as he was, had failed to sense the dying wretch before him as he crept closer to death by the second.

And Jin Taekyung was no different.

*Now.*

It was as if someone else, someone he couldn’t see, were whispering in his ear.

His vision was clouded white, and he couldn’t see a thing.

Time was running out. A horrible weariness—and an even stronger feeling of death—was seeping into his body.

*Shhk.*

Jin Taekyung thrust out his spear smoothly.

The shouts and screams of friend and foe, ringing out without pause even now. The cold clang of steel. The sound of a trumpet, now drawing close.

Even the palm the Blood Lord thrust out on instinct.

Nothing could stop him.

Leaving it all behind, as if it had been decided from the beginning, Jin Taekyung let the flames deep inside his body flow toward a single point.

*Thud.*

A spearhead carrying faint warmth pierced the palm wrapped in Force and drove through.

Past that very hand, whose wound, for some reason, had yet to heal.

KRRRCH!

The monster’s eyes flew wide, bulging as they filled with shock.
```
