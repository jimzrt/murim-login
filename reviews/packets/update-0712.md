<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0712.txt",
      "sha256": "7758d3bd45c4d33dbd881fe9d7216dce9b44f8c5f34eb5ab26cde6e057a1747e",
      "bytes": 13889
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7a423c2c17cb281165aa6fa69ca82695b4f4c45d1bf2c0125250e1977c657c43",
      "bytes": 1674
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c1986676bc48fdff4fd48cf0f0b57f97ebad0bdfdd8467f01fb8d3155af76b6e",
      "bytes": 207119
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "747a7386e220a507c630d7af981e438c3fc270bdca16020110f3d8b41cb7b3e6",
      "bytes": 792
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "4c6141da33a2acea9b98645c692d3118acd7ec7b8b8c2308f03f5440d904e662",
      "bytes": 553
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "0fcd83d245bc35fef59fc401d38be3676dfbbe4fe4ebfc822dd72365f59e78d5",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "d75ba5781de7350ae8b564f25b67b250fbddc5e30e498f15f0ea6140df3fe167",
      "bytes": 1949
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "7d8137cdf7ca0accaef50be9d5365c86dd0af510860c464efc417063b843041e",
      "bytes": 622
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "24e2572e0a06ad81b1a943ca3635e010c0a59140b47709bc7955aaa11124cdbd",
      "bytes": 676
    },
    {
      "path": "characters/White Tiger.md",
      "sha256": "fefe7e3ae43bdfae34cfe793786eddd6c5ce3dce66bd7cc9c36b29c9ad6cb524",
      "bytes": 560
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "60f6da52d25b48dc2329bdcd72aded72090a5b5c62924e9821844bd135b01f6f",
      "bytes": 217943
    }
  ],
  "estimated_tokens": 11843
}
-->

# Durable State Update — Chapter 712

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 712. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 712. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 712,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 712,
    "continuity_sources": [712],
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
    "Jin Taekyung has fully recovered through five System level-ups, but remains mentally exhausted after the battlefield.",
    "Jeok Cheongang is confirmed as the Blood Monk and has reunited with Jin Taekyung after fighting through Guangxi to reach him.",
    "The battlefield has only about thirty survivors from the Nanman warriors and Baekcheon Unit.",
    "Wang Ho survived after Jin treated his severe injuries.",
    "The Beast Miao King is unconscious and gravely injured, though Jeok believes he can survive treatment.",
    "The White Tiger is gravely wounded but conscious and intends to use the sacred stone to close the rift.",
    "The guardian spirit saved Jin and entrusted him with the sacred stone because he resembles the first Palace Lord of the Nanman Beast Palace."
  ],
  "continuity_sources": [
    711
  ],
  "open_questions": [
    "What is the Southern Heaven Demon Empress's final status after Jin's throat attack and Jeok's Flame Divine Palm?",
    "Will the Beast Miao King survive treatment?",
    "Will the White Tiger survive long enough to close the rift?",
    "What will happen to the sacred stone when the guardian spirit attempts to close the rift?",
    "What caused the bell and warmth accompanying Jin's recovery beyond the five level-ups?"
  ],
  "safe_through": 711,
  "temporary_decisions": [
    "Retain Blood Monk as Jeok Cheongang's revealed sobriquet.",
    "Retain Old Master for Jin Taekyung's address to Jeok Cheongang.",
    "Render the guardian spirit's 의념 as Will.",
    "Preserve Jeok Cheongang's gruff, profane dialogue and Jin Taekyung's dry first-person voice."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 노부      | **this old man / I**                                            |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 평화 | **Peace Guild** | Guild name. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 비도 | **throwing blade** | Mungyeong throws one past Taekyung's neck. |
| 변이체 | **mutant** | Taekyung's classification for the monster. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 수왕석 | **Beast King Stone** | Legendary sacred treasure of the Nanman Beast Palace. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 성지 | **Sacred Land** | Former name of the Poisonblood Grounds when beasts ruled Ailao Mountain. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |
| 신석 | **sacred stone** | Stone said to have existed alongside the Black Tiger's birth. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |
| 적천강 | 수신룡 | legendary_martial_master_to_dying_spirit_beast | you | wary and trembling | Jeok asks what the Water God Dragon is after witnessing its mental communication. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 진태경 | 부족장 | captor to captured tribal chieftain | tribal chieftain | casual, coercive, and mocking | Jin promises to spare the captured chieftain if he answers questions properly. |
| 부족장 | 진태경 | captured tribal chieftain to overpowering enemy | Jin Taekyung | alarmed and desperate | The chieftain recognizes Jin by name while fleeing and then begs for his life. |
| 백호 | 진태경 | guardian_spirit_to_human_ally | you | terse and irritated | The White Tiger responds telepathically after Jin calls it Whitey and jokes about its former name. |
| 진태경 | 수호령 | human ally to guardian spirit | guardian spirit | quiet and commanding | Jin whispers that they should go as they advance toward Baeksang. |
| 수호령 | 남천마후 | guardian_spirit_to_hostile_supernatural_opponent | you | terse, accusatory, and contemptuous | The guardian spirit tells the Southern Heaven Demon Empress that it knows her true essence and condemns her as a Fiend. |
| 남천마후 | 수호령 | hostile_supernatural_opponent_to_guardian_spirit | hideous beast | playful, taunting, and dismissive | She insults the guardian spirit while addressing it as a beast. |
| 수호령 | 진태경 | guardian spirit to human ally | Human | terse and alarmed | The guardian spirit cries out to Jin as the Southern Heaven Demon Empress sends him crashing into the ground. |
| 야수묘왕 | 남천마후 | allied_Ten_Kings_master_to_hostile_Demon_Empress | you | cold and threatening | The Beast Miao King addresses the Southern Heaven Demon Empress while promising to tear off her limbs and kill her. |
| 수호령 | 적천강 | guardian_spirit_to_legendary_martial_master | old human | terse and contemptuous | The guardian spirit addresses Jeok as 늙은 인간 while recognizing that his essence has not changed. |

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 711
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and Great Chieftain of the Miao people.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang is his sworn younger brother and childhood companion, Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple whom he now fights beside against the Southern Heaven Demon Empress.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 711
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 711
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 710
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license; he shielded the Southern Heaven Demon Empress from Jeok Cheongang's Flame Divine Palm, survived the resulting devastation, and began recovering after the attack.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 710
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 711
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is Honglan, the creator of the rift behind the Inner Palace.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### White Tiger.md

# White Tiger (백호)

- **Safe through:** Chapter 711
- **Aliases:** Whitey
- **Role:** The White Tiger is the guardian spirit of the sacred stone and leader of the Sacred Land beasts; it intends to use the sacred stone to close the rift.
- **Personality:** Irritable and contemptuous of Jin Taekyung's jokes.
- **Voice:** Telepathic, terse, and easily exasperated.
- **Relationships:** The White Tiger carries Jin Taekyung and Yohi, guards the sacred stone, and advances with Jin's forces.

## Korean source

```text
＃712화



아니었으면 했다.

지금 떠오른 이 생각이, 내 짐작이 모두 헛된 것이길 바랐다.

그러나 다음 순간 들려온 수호령의 의념에, 나는 그 모든 것이 사실임을 깨달았다.

- 누군가는 반드시 해야 할 일이다. 어쩌면 이것이 내게 주어진 운명일지도 모르겠군.

내가 본능적으로 수호령의 생각을 알아차린 것처럼, 그 역시 마찬가지였다.

모든 것을 꿰뚫어 볼 것처럼 맑고 투명한 청백색의 눈동자에 내 얼굴이 비쳤다.

- 저 어둠…… 너희가 균열이라 부르는 저것을 없애지 않는 한 모든 것은 끝나지 않는다. 아니, 또 다른 재앙의 시작이겠지.

부정할 수 없는 사실이었다. 치열한 악전고투 끝에 남천마후와 그 수하들을 처치했지만, 그들이 열어 놓은 균열은 여전히 남아 공간을 잠식해 나가고 있었다.

지금 이 순간조차도.

솨아아아.

이제 내궁을 넘어 외궁을 향해 나아가고 있는 어둠.

그 안에 스며들어 있는 마기(魔氣)는 살아 있는 것을 타락시키고, 이성을 잃은 존재로 변이시켜 또 다른 재앙을 불러올 것이다.

‘사실상 몬스터 군단이나 다름없겠지.’

게이트를 떠올리게 만드는 저 균열의 힘이 어디까지 미칠지는 알 수 없다.

그러나 만약 균열에서 흘러나온 마기가 남만을 집어삼킬 정도라면, 혹은 그 이상이라면 이 어둠은 끝없이 계속될 것이다.

남만을 넘어, 온 천하를 잠식할 때까지.

- 인간이여. 너 역시 짐작하고 있겠지만, 저 어둠을 감당할 수 있는 것은 오직 신석(神石)의 기운뿐이다. 누군가는 저 균열의 중심으로 들어가 신석과 함께 어둠을 견뎌 내야 하지.

나도 안다. 불과 몇 개월 전, 수신룡이 스스로를 바쳐 균열을 틀어막았으니까.

그리고 그 희생의 대가가 어떠했는지도 알고 있다.

“……만약 네가, 지금까지와는 다른 무언가가 된다면?”

차마 변이체가 된다는 말은 꺼낼 수 없었던 나를 향해, 수호령이 희미하게 웃었다.

- 나를 죽여라. 한 치의 망설임도 없이.

“……!”

- 너와 저 늙은 인간의 힘이라면, 설령 내가 타락한 존재가 되더라도 그리 어렵지 않을 것이다.

수호령을 말없이 바라보던 나는, 힘겹게 입을 열었다.

그것은 처음 수호령의 뜻을 알아차린 순간부터 마음속에 간직하고 있던 생각이었고, 긴 고민 끝에 나온 한 마디였다.

“만약, 만약 내가 직접 균열을 막는다면?”

그리고 그 물음에 대한 대답은, 수호령이 아닌 다른 곳에서 나왔다.

“말도 안 되는 소리!”

야수묘왕의 내상을 다스리고 있던 적천강의 외침이다.

어느 때보다 굳은 얼굴을 한 그가 나를 바라보며 말을 이었다.

“불가(不可). 네놈이 무슨 말을 지껄여도 노부는 허락할 수 없다.”

“하지만 노야…….”

“듣기 싫다. 네놈이 아무리 뛰어난 성취를 이루었다 한들, 무슨 일이 벌어질지 모르는데 어찌 허락할 수 있겠느냐.”

“털끝 하나 다치지 않고 멀쩡하게 돌아오겠습니다. 약속드릴게요.”

“털끝 하나 다치지 않고?”

“예.”

고개를 끄덕인 나를 말 없이 응시하던 적천강이 입을 열었다.

“네 뜻이 정 그렇다면. 좋다.”

“그럼…….”

“네놈은 이곳에 남아 있거라. 노부가 갈 테니.”

“……!”

“네놈이 몸 성히 돌아올 수 있을 정도라면, 차라리 노부가 가는 것이 더 확실하겠지. 내 말이 틀렸느냐?”

정곡을 찌르는 한 마디에 순간 말문이 막혀 버린 그때, 수호령의 의념이 울려 퍼졌다.

- 늙은 인간이여. 만약 저 젊은 인간이 어둠에 의해 지금과는 다른 존재가 된다면, 넌 어찌할 테냐.

“저 아이를 죽일 거다. 안식을 되찾을 수 있도록.”

한 치의 망설임도 없이 대답한 적천강이, 낮은 목소리로 말을 이었다.

“그리고 노부 역시 죽음을 택하겠지.”

- 젊은 인간이여, 그 반대의 경우에 너는 어찌하겠느냐?

나는 대답하지 않았고, 침묵의 의미를 꿰뚫어 본 수호령은 빙긋 웃어 보였다.

- 그래, 그것이 내가 가야 하는 이유다.

“…….”

- 이 땅의 인간들은 이미 많은 피를 흘렸다. 그러니 너와 저 늙은 인간이 나를 대신하여 희생할 이유는 그 어디에도 없다. 너희에게는 아직 많은 운명이 남아 있고, 나는 이미 많은 운명을 거쳐 왔으니.

수호령이 청백색의 눈동자를 들어 적천강을 응시했다.

- 설령 돌이킬 수 없는 상황이 된다면, 망설이지 말고 나를 죽여라.

적천강이 작게 고개를 끄덕였다.

“전력을 다하지.”

- 고맙군.

그르릉. 힘겹게 숨을 몰아쉰 수호령이 나를 향해 입을 벌렸다.

- 진태경. 이제 시간이 되었다.

더 이상 무슨 말을 할 수 있을까.

나는 품에 손을 집어넣으며 마음속으로 중얼거렸다.

‘인벤토리 오픈. 소환.’

그리고 다음 순간, 수호령에게 내민 손바닥 위에는 따스하고 희미한 빛을 뿜어내는 무언가가 있었다.

그 신비한 기운을 느낀 적천강이 신음처럼 중얼거렸다.

“이건 설마…….”

- 너희 인간들이 수왕석이라 부르는 이 신석은, 내게 남은 유일한 사명이자 존재하는 이유였다. 그리고 이제, 그 마지막까지 함께하게 되겠구나.

스아아아.

서서히 허공으로 떠오른 신석이 수호령의 입안으로 빨려 들어간다.

희미한 광휘와 함께 번져 나가는 온기.

그와 동시에 헐떡이던 수호령의 호흡이 안정되고 힘없이 쓰러져 몸뚱어리가 조금씩 힘을 되찾기 시작했다.

스륵. 쿵.

마침내 몸을 일으킨 거대한 백호가 피에 젖은 앞발을 내디뎠다.

저벅. 저벅.

한 걸음. 또 한 걸음.

그 어느 때보다 무거운 발걸음이었으나, 누구도 막을 수 없는 걸음이기도 했다.

그것은 처음과는 비교도 할 수 없을 만큼 짙고, 끈적해진 어둠조차 마찬가지였다.

콰아아아.

사방에 가득한 피 웅덩이와 곳곳에 널브러진 숱한 시신들. 그 위를 타 넘어 파도처럼 덮쳐 오던 어둠이 수호령을 둘러싼 빛에 부딪쳐 물러난다.

균열로부터 흘러나온 어둠이 모든 것을 오염시킨다면, 신석이 머금은 빛은 정화(淨化)의 힘이었다.

- 크아아앙!

거센 포효가 천지를 떨어 울린다. 붉게 물든 은빛 갈기가 세차게 흩날렸다.

어느새 수호령은 한 줄기의 바람이 되어 달려 나가고 있었다.

쐐애애액!

나는 어둠을 가르며 쏘아지는 수호령의 뒷모습을 바라보았다.

희미하지만 어느 것보다 또렷하게 빛나는 그 섬광이, 수많은 시체와 잔해를 가로지를 때까지.

너른 공간을 달려 칠흑과도 같은 어둠에 잠긴 절벽에 다다를 때까지.

그리고 문득 깨달았다.

마지막 순간, 수호령이 처음으로 내 이름을 불러주었다는 것을.



* * *



숨이 찼다. 피에 흠뻑 젖은 몸뚱어리는 무거웠고, 사방에 가득한 어둠은 수호령의 전신을 옥죄었다.

‘이무기여. 그대도 이런 기분이었나.’

들리지 않을 물음과 함께, 수호령은 쩍 벌어진 절벽 틈새로 온 힘을 다해 걸음을 내디뎠다.

힘겹더라도 가야 한다.

과거에는 몰랐지만, 이제는 알기 때문이다.

이것만이 처음부터 자신에게 주어진 유일한 사명이었다는 것을. 수호령이 지켜야 하는 것은 신석이 아닌, 바로 이 땅의 모든 것이었다.

콰득.

그 어느 때보다 무거운 발걸음이 지면 깊숙이 파묻힌다. 균열의 중심에 다가갈수록, 더욱 강대해진 어둠과 마기가 수호령의 전신을 짓누르고 있었다.

흐릿한 의식 속에서 까마득한 옛 기억들이 청백색 눈동자를 스쳐 지나갔다.

‘생각해 보면 늘 혼자였지.’

아비도, 어미도, 형제도 없었다.

아니, 처음에는 그런 것이 세상에 존재하는지조차도 몰랐다.

어느 작고 새하얀 백호에게는 처음 눈을 떴을 때부터 보였던 이 공간이 세상 그 자체였고, 언제나 함께했던 친구가 있었으니까.

함께 뛰며 놀 수도 없고, 말도 통하지 않지만 언제나 자신의 곁에 있던 친구가.

툭.

솜뭉치처럼 부드럽고 새하얀 앞발에 닿은 무언가.

그것은 수정(水晶)이라 부르는 것이 더 어울릴 만큼 투명한 돌이었고, 언제나처럼 따뜻하고 편안했다.

그르릉.

기분 좋은 울음소리를 흘린 어린 백호는 얼마 지나지 않아 새근새근 잠들었다.

그리고 햇빛도, 달빛도 아닌 따스한 빛이 쏟아지는 어느 언덕에서 잠이 든 백호의 발치에서, 초록빛 새싹이 불쑥 고개를 내밀었다.

스륵. 툭.

손톱만큼 작았던 새싹이 굽혔던 허리를 펴기 시작했다. 형형색색의 꽃망울을 틔우고 가지가 생겨났다.

어느덧 새싹이 있던 자리에는 땅 깊숙이 뿌리내린 거목(巨木)이 우뚝 서 있었고, 수많은 가지에 매달린 잎사귀들은 넓고 시원한 그늘을 드리웠다.

솨아아아.

어디선가 불어온 바람에, 거목이 풍성한 머리를 흔들었다.

제법 끈질기게 버티고 있던 잎사귀 하나가 가지를 벗어나 그늘로 떨어졌다.

툭, 하고 부딪히는 감촉과 함께 낮잠을 즐기던 어느 존재가 눈을 떴다.

- 크릉.

낮은 울음소리와 함께 몸을 일으킨 존재의 정체는 한 마리의 백호였다.

더 이상 새끼라 보기에도, 평범한 호랑이라 부르기에도 너무나 거대해지고 강력한 힘을 지니게 된 백호는 청백색의 눈동자로 주위를 둘러보았다.

시간이 얼마나 흘렀는지, 정확히는 그 누구도 몰랐다.

그저 적지 않은 시간이 흘렀다는 것만 짐작할 뿐. 그가 태어나고 자란 이곳은 언제나 낮이었고 평화로웠으니까.

하지만 그럼에도 불구하고 변화는 있었다.

새싹이 거목으로 자라나고, 작고 부드럽던 새끼 백호가 거대하고 강력한 존재로 거듭난 것만큼이나 확실한 변화가.

‘그래, 그 녀석.’

그를 처음 만난 건 삼백 년 전의 일이었다. 곰처럼 커다란 체구와 맞지 않게 늘 싱글벙글 웃고 있던 그는 인간들을 이끄는 부족장이었고, 짐승들을 따르게 하는 신비로운 힘을 지녔었다.

아마도 그래서였을 것이다. 수호령의 허락 없이도, 성지의 짐승들이 그를 받아들인 이유는.

‘오. 이렇게 큰 백호는 또 처음 보네. 넌 이름이 뭐니?’

처음에는 자신의 허락 없이 성지에 발을 디딘 인간이 있다는 사실이 놀라웠고, 그 인간 놈이 겁도 없이 목덜미를 쓰다듬었을 때는 어이가 없었다.

그래서 물었다.

‘그러는 네놈의 이름은 무엇이냐?’

버르장머리 없는 인간 놈이 지었던 표정은 아직도 생생하다. 입을 딱 벌린 채 수호령을 바라보던 그는 얼빠진 목소리로 대답했다.



‘야율천……인데요.’

‘어떻게 이곳에 들어왔는지는 모르나, 다시 한번 이 몸의 눈에 띈다면 사지를 찢어 죽일 것이다. 알겠느냐?’



그리고 다음 날, 수호령은 깨달았다.

야율천이라는 저 젊은 인간 놈이, 자신이 지금까지 봐 왔던 어떤 생명체보다 겁대가리가 없다는 것을.



‘분명히 눈에 띄지 말라고 했을 텐데.’

‘그래서 숨어 있었는데요.’

‘……지금 장난하는 건가?’

‘냄새 때문에 안 거지, 보고 있는 게 아니잖아요. 저 지금 풀숲에 엎드려 있어요.’

‘아니, 그걸 지금 말이라고…… 그런데 이 냄새는 뭐지?’

‘구운 고기요. 배고플까 봐 챙겨 왔는데 좀 드실래요?’

‘고기? 혹시 짐승들을 사냥했나?’

‘…….’



어떻게 그 녀석과 가까워졌는지는 모른다. 다만 가랑비에 몸이 젖듯 그들은 서서히 서로를 알게 되었고, 그 과정 속에서 시간은 빠르게 흘렀다.

십 년. 이십 년. 그리고 그들이 마지막으로 서로를 마주했던 그날까지.

‘오랜만이구려.’

몇 년 만에 찾아온 그는 더 이상 청년이 아니었다.

검었던 머리는 어느새 반백이 되어 버렸고, 눈은 피로에 지쳐 있었다.

‘도움이 필요하오. 그대와 신석의 힘이 있어야만 이 전쟁에서 승리하고 남만의 평화를 되찾을 수 있소.’

수호령은 알고 있었다. 그가 어떤 싸움을 하고 있는지, 그들의 적이 얼마나 악한 인간들인지.

하지만 거절했다.

신석은, 자신은 그저 관조자에 불과하니까. 그때는 그렇게 생각했다.

적어도 그때에는.

그리고 후회는 언제나 늦었다.

‘그때 널 도왔다면, 이 땅의 운명은 바뀌었을까.’

깊게 가라앉아 있던 청백색의 눈동자가 상념에서 깨어난다.

눈앞에서 휘몰아치는 혼탁한 어둠이 보인다. 기이하게 일렁이는 그것은 모든 것을 집어삼킬 듯이 마기를 토해 내고 있었다.

츠츠츠츠츠!

일그러지는 공간 속. 힘겹게 마지막 걸음을 옮긴 수호령은 균열의 중심을 응시했다.

그리고 온 힘을 다해, 희미한 빛이 서린 몸을 움직여 달려들었다.

- 크아아아앙!

한 줄기의 포효와 함께, 거대한 파동이 터져 나왔다.
```

## Final English reading copy

```markdown
# Chapter 712

I hoped I was wrong.

I wanted this thought that had just crossed my mind—this suspicion of mine—to be completely unfounded.

But when the guardian spirit’s Will reached me the next moment, I realized that all of it was true.

—Someone has to do it. Perhaps this is the fate I was given.

Just as I had instinctively understood the guardian spirit’s thoughts, it had done the same.

My face was reflected in its clear, transparent blue-white eyes, so pure they seemed capable of seeing through everything.

—Until that darkness… that thing you call a rift is gone, nothing will end. No, it will be the beginning of another catastrophe.

It was an undeniable fact. We had defeated the Southern Heaven Demon Empress and her subordinates after a fierce, grueling struggle, but the rift they had opened still remained, devouring the space around it.

Even now.

Ssshhhhhh.

The darkness had already passed beyond the Inner Palace and was advancing toward the Outer Palace.

The demonic qi seeping through it would corrupt living things, transform them into beings that had lost their reason, and bring about another disaster.

*It would basically be an army of monsters.*

There was no way to know how far the rift’s power—which reminded me of a Gate—would reach.

But if the demonic qi flowing from the rift was enough to swallow Nanman, or even more than that, this darkness would continue without end.

Until it consumed the entire world beyond Nanman.

—Human. As you have likely guessed, only the power of the sacred stone can withstand that darkness. Someone must enter the center of the rift and endure the darkness alongside the sacred stone.

I knew that, too. Only a few months ago, the Water God Dragon had sacrificed itself to seal the rift.

And I knew what the price of that sacrifice had been.

“What if you become something different from what you’ve been until now?”

I couldn’t bring myself to say that it would become a mutant. The guardian spirit smiled faintly at me.

—Kill me. Without the slightest hesitation.

“……!”

—With your strength and that old human’s, it shouldn’t be too difficult, even if I become a corrupted being.

I stared at the guardian spirit in silence before forcing my mouth open.

It was the thought I had held in my heart from the moment I first understood the guardian spirit’s intentions, and the single question I had reached after a long period of deliberation.

“What if I seal the rift myself?”

The answer to that question came from somewhere other than the guardian spirit.

“Don’t be ridiculous!”

It was Jeok Cheongang’s shout. He had been tending to the Beast Miao King’s Internal Injury.

His expression was graver than ever as he looked at me and continued.

“Impossible. No matter what you say, this old man cannot allow it.”

“But, Old Master—”

“I don’t want to hear it. No matter how great an achievement you’ve made, we have no idea what might happen. How could I allow it?”

“I’ll come back safe and sound without so much as a hair out of place. I promise.”

“Without so much as a hair out of place?”

“Yes.”

I nodded, and Jeok Cheongang stared at me silently before opening his mouth.

“If that is truly your wish. Very well.”

“Then—”

“You will stay here. This old man will go.”

“……!”

“If you can return without a scratch, then it would be even more certain if I went instead. Am I wrong?”

His single remark had struck the heart of the matter, and for a moment I couldn’t get a word out.

Then the guardian spirit’s Will rang out.

—Old human. If that young human becomes a different being because of the darkness, what will you do?

“I’ll kill that child. So he can find peace.”

Jeok Cheongang answered without the slightest hesitation, then continued in a low voice.

“And this old man will choose death as well.”

—Young human, what will you do in the opposite situation?

I didn’t answer, and the guardian spirit saw straight through the meaning of my silence. It smiled faintly.

—Yes. That is why I must go.

“……”

—The humans of this land have already shed enough blood. There is no reason for you and that old human to sacrifice yourselves in my place. You still have many fates ahead of you, while I have already passed through many fates.

The guardian spirit raised its blue-white eyes and looked at Jeok Cheongang.

—Even if the situation becomes irreversible, do not hesitate to kill me.

Jeok Cheongang gave a small nod.

“I’ll give it everything I have.”

—Thank you.

Grrr. The guardian spirit drew a labored breath, then opened its mouth toward me.

—Jin Taekyung. The time has come.

What more could I say?

I reached into my robes and muttered inwardly.

*Inventory open. Summon.*

The next moment, something that gave off a warm, faint light rested on my outstretched palm before the guardian spirit.

Jeok Cheongang felt its mysterious energy and muttered like he was groaning.

“Don’t tell me this is…”

—This sacred stone, which you humans call the Beast King Stone, was my only remaining mission and the reason for my existence. And now, it seems we will be together until the very end.

Ssshhhh.

The sacred stone slowly floated into the air and was drawn into the guardian spirit’s mouth.

Warmth spread outward with its faint radiance.

At the same time, the guardian spirit’s panting grew steadier, and the body that had collapsed helplessly began to regain its strength.

Rustle. Thud.

At last, the enormous White Tiger rose and planted one blood-soaked forepaw on the ground.

Thud. Thud.

One step. Then another.

Its footsteps were heavier than ever, but they were also footsteps no one could stop.

Not even the darkness, now incomparably denser and stickier than at first, could stop them.

Kraaaash!

Pools of blood filled the surroundings, and countless corpses lay strewn everywhere. The darkness that had surged over them like a wave struck the light surrounding the guardian spirit and recoiled.

If the darkness flowing from the rift corrupted everything, then the light contained within the sacred stone possessed the power of purification.

—Kraaaaang!

A fierce roar shook heaven and earth. Its silver mane, stained red, whipped violently in the wind.

Before I knew it, the guardian spirit had become a gust of wind and was racing forward.

Shweeeek!

I watched the guardian spirit’s back as it shot through the darkness.

I watched until that faint but unmistakably brilliant streak of light crossed countless corpses and remnants.

Until it raced across the vast space and reached the cliff swallowed by pitch-black darkness.

And then I realized something.

At the very end, the guardian spirit had called my name for the first time.

* * *

It was out of breath. Its body was drenched in blood and heavy, while the darkness filling the surroundings constricted the guardian spirit from head to toe.

*Imugi. Did you feel this way, too?*

With that unheard question, the guardian spirit took a step with all its strength into the gaping fissure in the cliff.

It had to go, no matter how difficult it was.

It had not known before, but now it did.

This was the only mission it had been given from the beginning. What the guardian spirit had to protect was not the sacred stone, but everything in this land.

Crack.

Its footsteps were heavier than ever, sinking deep into the ground. The closer it came to the center of the rift, the more powerful the darkness and demonic qi became, pressing down on its entire body.

Through its fading consciousness, memories from the distant past flashed across its blue-white eyes.

*Come to think of it, I was always alone.*

It had no father, mother, or siblings.

No. At first, it did not even know whether such things existed in the world.

To one small, pure-white White Tiger, this space it had seen from the moment it first opened its eyes was the world itself. And it had a friend who had always been there with it.

A friend who could not run and play alongside it, and with whom it could not communicate, but who had always remained by its side.

Tap.

Something touched its soft, pure-white forepaw, as gentle as a ball of cotton.

It was a transparent stone, so clear that crystal would have been a more fitting name for it. As always, it was warm and comforting.

Grrr.

The young White Tiger let out a contented growl and soon fell asleep, breathing softly.

And at the feet of the sleeping White Tiger, on a hill drenched in warm light that was neither sunlight nor moonlight, a green sprout suddenly pushed its head above the ground.

Rustle. Tap.

The sprout, which had been no larger than a fingernail, began to straighten its bent stem. It burst into colorful buds, and branches began to grow.

Before long, where the sprout had once been stood a giant tree with roots sunk deep into the earth. Its leaves, hanging from countless branches, cast a broad, cool shade.

Ssshhhh.

A wind blew from somewhere, and the giant tree shook its full crown.

One leaf that had held on stubbornly for quite some time finally broke away from its branch and fell into the shade.

At the soft tap of the leaf landing on it, a being enjoying an afternoon nap opened its eyes.

—Grrr.

The being rose with a low growl.

It was a White Tiger.

It had grown too enormous and powerful to be called a cub, or even an ordinary tiger. It looked around with its blue-white eyes.

No one knew exactly how much time had passed.

They could only guess that quite a lot of time had gone by. It was always daytime in the place where it had been born and raised, and it had always been peaceful.

But even so, there had been change.

Change as certain as the sprout growing into a giant tree, or the small, soft White Tiger cub becoming a huge and powerful being.

*Yes, that one.*

It had first met him three hundred years ago. Despite his bear-like size, he was always grinning broadly. He was a tribal chieftain who led humans and possessed a mysterious power that made beasts follow him.

That was probably why the beasts of the Sacred Land had accepted him even without the guardian spirit’s permission.

“Oh. I’ve never seen a White Tiger this big before. What’s your name?”

At first, the guardian spirit had been surprised that a human had set foot in the Sacred Land without its permission.

When that human bastard fearlessly reached out and stroked the back of its neck, the guardian spirit had been left speechless.

So it asked him.

“And what is your name, then?”

The expression on the insolent human bastard’s face was still vivid in its memory. He had stared at the guardian spirit with his mouth hanging open, then answered in a dazed voice.

“Yayul Cheon….”

“I do not know how you entered this place, but if I see you here again, I will tear you limb from limb and kill you. Do you understand?”

And the next day, the guardian spirit realized something.

That young human bastard named Yayul Cheon had less fear than any living creature it had ever seen.

“I believe I told you not to let yourself be seen.”

“That’s why I was hiding.”

“……Are you joking with me right now?”

“You knew because of my smell, not because you saw me. I’m lying face-down in the grass right now.”

“No, is that supposed to be an answer? …Wait. What is that smell?”

“Grilled meat. I brought some in case you were hungry. Want some?”

“Meat? Did you hunt the beasts?”

“……”

It did not know how it had grown close to him. They simply came to know each other little by little, like clothes slowly soaking through in a drizzle, and time passed swiftly in the process.

Ten years. Twenty years. And then, the day they last faced each other.

“It’s been a long time.”

When he came to visit after several years, he was no longer a young man.

His black hair had already turned half gray, and his eyes were worn out with fatigue.

“I need your help. Only with your power and that of the sacred stone can we win this war and restore peace to Nanman.”

The guardian spirit knew what kind of battle he was fighting, and how evil their enemies were.

But it refused.

The sacred stone and the guardian spirit were nothing more than observers. That was what it thought then.

At least, it had thought so at the time.

And regret always came too late.

*If I had helped you then, would the fate of this land have changed?*

The blue-white eyes, sunk deep in thought, came back to the present.

Turbulent darkness churned before them. It writhed strangely and spewed demonic qi as though it intended to swallow everything.

Ssssss!

Within the warped space, the guardian spirit struggled through its final step and stared at the center of the rift.

Then, with every bit of strength it possessed, it moved its body wrapped in faint light and lunged forward.

—Kraaaaang!

With a single roar, an enormous shock wave burst outward.
```
