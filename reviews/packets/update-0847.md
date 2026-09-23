<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0847.txt",
      "sha256": "cea026b1c635faf59c1cce062c2cae8c545dd43d0bab59c78e194af25734ee91",
      "bytes": 14552
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "54394a53215aef6744a4b48c9945203bf1fb633e53d02c6cbe9657f639315cf0",
      "bytes": 3071
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "254d5811f77ef1fdb1ad72eee4b3a738d6293cd2217858cff6f86dabc0ccb323",
      "bytes": 227491
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "96dfdf6e9b975819f2172b0871ce6400d93580fe28dbddafbe3ffbb2d2682e1e",
      "bytes": 759
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "73d7ab9887780f637a6d6a130d372d02ec8406bad50800b2a09e191f2a269724",
      "bytes": 1573
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "9ed3a84d64cb859c01c1eacafde5813e200c4d5131362481ce1a2ed7156c35d2",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "21f8efba8605e20882dffcb6d0a1df6c41db118f9388e4997b0c021793e64334",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ef87894d7e6e58370eefc26a6e542406cf849311afb057ed00381198bbe91265",
      "bytes": 252436
    }
  ],
  "estimated_tokens": 11368
}
-->

# Durable State Update — Chapter 847

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
1 and safe_through 847. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 847. Profile updates may replace only one
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
  "chapter": 847,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 847,
    "continuity_sources": [847],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader.",
    "The supernatural Rift began at 10%; its progress increases the distribution and concentration of magical power.",
    "The System’s Status Window is inaccessible; Jin suspects an update may be responsible.",
    "Jin’s vision of a black-haired man killing Ahomed after the ritual remains unexplained; Jin believes the man was not Asmodeus.",
    "Jin’s [Broken Body] injury and damaged vital essence remain unresolved; the Divine Physician says full recovery is impossible but improvement is possible.",
    "Jin is at the Sichuan Tang Clan, where the Divine Physician’s pill was absorbed through Jeok Cheongang’s treatment; Jin is unconscious.",
    "Jeok Cheongang and Jin Taekyung trust each other deeply; their Master-Disciple bond remains unformalized.",
    "The Sichuan Tang Clan and Sichuan Murim are rebuilding after Dark Heaven’s attack; allied martial artists remain to treat patients and guard against another attack.",
    "Dark Heaven developed experimental seeds over years of research and scattered some across the Central Plains; some have already blossomed.",
    "The Blood Lord ordered sorcerers to prepare selected seeds for later deployment and sent missives by hawk.",
    "The Lord of Heaven recently ordered the Blood Lord to bring down the heavens, then returned to sleep.",
    "The City Lord of Seongju is gravely ill, with alternating lucidity and violent episodes; after returning from the Imperial Capital, he lost his favored concubine Aehyang to the Son of Heaven."
  ],
  "continuity_sources": [
    845,
    846
  ],
  "open_questions": [
    "Why did the Main Quest fail despite the Doppelganger’s erasure, and who or what was summoned?",
    "Was Jin’s vision of the summoned being real, System-delivered, or prophetic?",
    "What will happen as the Rift progresses and more beings enter the world?",
    "Who or what chose Jin, what is the Ark, and how did Dark Heaven reach Murim?",
    "What are Dark Heaven’s seeds, what effects are the experiments meant to enhance, and what caused the City Lord’s illness?"
  ],
  "safe_through": 846,
  "temporary_decisions": [
    "Keep magical power distinct from mana; keep Blink distinct from Teleport and Warp. Extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells; render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” and 실드 마법 as “Shield magic.”",
    "Render 선택받은 자 as “the Chosen One,” 방주의 주인 as “the Master of the Ark,” [격변] as [Cataclysm], [어데 도씹니꺼] as “Where’s Your Do Clan From?,” and [종족 학살자] as “Species Slayer.”",
    "Render 균열 as a social fracture or division, not the supernatural Rift; render 醜王 as “Disgrace King” when used as Jin’s mocking imagined epithet for Jeok Cheongang.",
    "Render 천자 as “Son of Heaven” and 애향 as “Aehyang.”"
  ],
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
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 낭인     | **wandering martial artist**                     |                                                       |
| 정파     | **orthodox faction**                             |                                                       |
| 제자     | **Disciple**                                 |
| 생도     | **cadet**                                    |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 백중 | **Baekjung** | Traditional Buddhist observance during which the Shaolin attack occurs. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 호위장 | **Captain of the Guards** | The Sichuan City Lord's guard captain. |
| 인자 | **ninja** | Japanese assassin skilled in concealment and concealed weapons. |
| 저승사자 | **Grim Reaper** | Mungyeong's threatening self-description during the banter. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |
| 적천강 | 호위장 | martial artist to official subordinate | you; bastard | blunt and threatening | Jeok uses familiar, insulting address while interrogating the Captain of the Guards. |
| 호위장 | 적천강 | official subordinate to senior martial artist | Sir | deferential | The Captain shifts to respectful speech after sensing Jeok’s status and danger. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 846
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 846
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; they trust each other deeply but have never formalized their bond. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to the late Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and is a long-standing rival of Peng Cheolhu.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 845
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 845
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃847화



천하는 광활하다.

그러나 천하(天下)라는 두 글자에 담긴 의미 그대로, 그 모든 것의 위에는 하늘이 있었다.

드넓은 대지와 바다. 살아 있는 것과 죽은 것.

그 무엇 하나 하늘을 피해 숨을 수 없다.

구름과 함께 아득한 창공을 가로지르는 날짐승조차, 끊임없이 번영과 몰락을 거듭하며 서로를 향해 날붙이를 겨누는 인간들조차 하늘을 우러러본다.

과연 저 위에는 어떤 대단한 존재가 있을까 하는 의문과 함께.

사람들에게 있어 하늘이란 바로 그런 것이었다.

그저 바라보기만 할 뿐, 결코 닿을 수 없는 미지의 영역. 두려워하면서도 공경해 마지않는 대상.

그렇기에 천하를 손에 넣은 이가 천자(天子)라 불리게 된 것은, 어쩌면 너무나도 당연한 일이었을 것이다.

세상 모든 것을 내려다보는 저 푸른 하늘이야말로 절대적인 권위의 상징이었으니까.

‘하지만 그런 천자도 결국 한낱 인간이지. 다른 이의 애첩까지 빼앗는 걸 보면.’

조금 전의 놀라움은 순식간에 사라지고 실소가 빈자리를 채운다.

피식 웃는 적천강의 모습에 호위장이 떨떠름한 표정을 지었다.

“그리 웃긴 이야기는 아니었습니다만.”

“아니, 듣는 입장에서는 충분히 우스웠다. 결국 천자라고까지 불리는 자가 신하의 애첩을 빼앗고, 그 신하가 상사병에 걸려 사경을 헤맨다는 소리니까.”

“……!”

경악한 호위장은 숨 쉬는 것조차 잊었다.

미친놈이라는 것 정도는 짐작했지만, 아무리 그래도 천자를 향해 저런 불경한 말을 내뱉다니.

황급히 주위의 인기척을 확인한 그는 간신히 목소리를 쥐어 짜냈다.

“미, 미쳤습니까? 귀하가 누구인지는 모르지만 어찌 감히 황상 폐하께……!”

“왜, 겁이라도 나느냐?”

“그걸 말이라고 하십니까? 세상에, 다른 누군가가 들었다면 당장 반역죄로 몰렸을 겁니다.”

“흠, 반역죄라.”

잠시 생각하던 적천강이 턱을 긁적였다.

예전 같았으면 모를까, 지금은 엄연히 제자를 둔 스승이자 무림맹에 속한 몸이었다.

“그건 좀 곤란해질 수도 있겠군.”

“곤란하다니. 무슨 반역죄가 무슨 경범죄인 줄 아시는 겁니까?”

“그렇다고 구족(九族)을 멸할 만큼 큰 죄는 아니지. 천자도 결국 피륙으로 이루어진 사람일진대, 욕 좀 얻어먹는다 한들 무엇이 대수란 말이냐.”

“……!”

“네놈 얼굴이 참 볼만하구나. 크흐흐.”

입만 딱 벌린 채 굳어 버린 호위장의 모습에, 적천강은 무릎을 치며 웃었다.

이미 일백하고도 수십여 년을 살아온 그다.

핏물이 마르지 않던 군웅할거(群雄割據)의 시대도, 새로운 통일 왕조의 탄생도 두 눈으로 직접 지켜보았다.

천자에 대한 환상? 경외?

웃기는 소리.

아주 오랜 과거부터, 적천강에게 있어 천자라는 호칭이 가지는 의미는 그리 각별하지 않았다.

‘그저 남들보다 조금 더 비범하며, 훨씬 더 큰 야망과 잔혹함을 지닌 자.’

그것이 바로 적천강의 평가였고, 하나뿐인 제자의 말을 들은 후에는 더더욱 확신할 수 있었다.

자신의 평가가 정확했다는 것을.

천자는 하늘이 내리는 것이 아니라, 무수한 피와 시체 속에서 태어난다는 것을.

적천강은 문득 진태경에게 들었던 이야기를 떠올렸다. 거대한 강철의 새를 하늘에 띄우고, 무수한 별들 사이를 누빈다는 그 놀라운 이야기들을.

그런 생각과 함께 얼어붙어 있는 호위장의 모습을 보니, 다시 한번 터져 나오는 실소를 참을 수 없었다.

“이해한다. 노부의 식견으로도 알지 못한 것이 산더미거늘, 네놈 같은 핏덩이가 어찌 짐작이나 할 수 있겠느냐.”

“노, 노부? 핏덩이?”

“세상은 넓고, 세월은 계속해서 흐른다. 아마도 삼천갑자 동방삭이라면 그 변화를 지켜볼 수 있겠지.”

호위장은 넋이 나간 얼굴로 적천강을 바라보았다.

기껏해야 동년배로 보이는 자가 구사하는 어휘가 너무 이질적인 탓도 있었지만, 그로서는 무엇 하나 이해할 수 없는 이야기들이기 때문이었다.

“그게 도대체 무슨 소리…….”

호위장이 말꼬리를 흐린 그때.

“굳이 이해하려 하실 필요는 없습니다. 저런 이야기를 듣는다면 누구나 같은 의문을 품을 테니까요.”

“……!”

불현듯 귓가를 파고든 누군가의 목소리에, 헛숨을 삼킨 호위장은 본능적으로 허리춤에 찬 검을 뽑아 휘둘렀다.

아니, 그러려고 했다.

어디선가 터져 나온 끔찍하리만치 거대한 기운이, 그의 전신을 짓누르기 전까지는.

화아악!

불길처럼 뜨겁고, 만근거석처럼 무거운 기파(氣波).

호위장은 감히 숨도 쉬지 못한 채 굳어 버렸다.

어느덧 머리 위를 짓누르는 기운을 이기지 못하고 푹 꺾여 버린 고개.

격동으로 파르르 떨리는 그의 시선은, 검 자루에 닿지도 못한 자신의 손을 향하고 있었다.

‘어, 어떻게?’

새하얗게 물든 호위장의 머릿속에서는 해결하지 못한 그 의문만이 둥둥 떠다녔다.

어찌 이럴 수 있단 말인가.

안락한 삶을 위해 무림을 떠나 관에 투신했어도 그는 절정 고수다.

그것도 명문대파의 그늘에서 자란 온실 속 화초가 아닌, 실전이라면 이골이 난 낭인(浪人) 출신의 절정 고수.

낭인으로 지낸 세월만 이십여 년이다.

솜털이 나기 시작할 때쯤 전장에 뛰어들었고, 끈질긴 잡초가 되어 살아남았다.

명문의 제자들처럼 훌륭한 무공을 익히지는 못했으나 사선(死線)을 넘나들며 쌓아 올린 경험은 그 이상이라고 자부했다.

그런데…….

‘움직이면, 죽는다.’

선명하게 보인다. 또렷하게 느껴진다.

성큼 다가온 죽음의 그림자가, 몇 번을 다시 태어난다 하더라도 결코 넘을 수 없을 거대한 벽이.

툭.

어느샌가 맺힌 식은땀 한 방울이, 호위장의 턱 끝을 타고 떨어져 내린 그 순간이었다.

“날도 더운데, 손님을 상대로 장난이 과하십니다.”

스아아.

문득 들려온 평온한 목소리에 언제 그랬냐는 듯 흩어지는 열기.

참았던 숨을 토해 내며 거칠게 심호흡하는 호위장의 귓가에, 두런두런 나누는 대화 소리가 전해졌다.

“손님은 무슨. 부탁 같지도 않은 부탁을 하러 온 어중이떠중이일 뿐이다.”

“정확히는 제 손님이지요. 애당초 저를 찾아오셨으니.”

“세상천지에 어떤 손님이 다짜고짜 검부터 뽑으려 든단 말이냐?”

“이해합니다. 넋이 나가 있는 상황에서 갑작스럽게 놀라면 그럴 수도 있는 것 아니겠습니까.”

“시끄럽다. 네놈은 노부 덕분에 무사한 줄이나 알아라.”

“감히 적 대협께 비할 수는 없겠으나, 저 역시 스승께 배운 한 수가 있으니 걱정하지 않으셔도 됩니다.”

“아니, 그런데 이 머리에 피도 안 마른 놈이 아까부터 따박따박 말대꾸를……!”

“의원으로서 견해를 말씀드리자면, 머리가 피가 마르면 죽습니다.”

“마!”

대화를 듣던 호위장은 혼란스러움을 느끼며 고개를 들었다.

머리에 피도 안 마르긴커녕, 새하얀 백발을 늘어트린 노인이 인자한 눈빛으로 그를 바라보고 있었다.

“괜찮으십니까?”

“……!”

그 순간. 호위장은 본능적으로 노인의 정체를 알아차렸다.

흡사 신선과도 같은 풍모. 거기에 더해 앞서 들었던 대화 속에 모든 답이 있었다.

“시, 신의(神醫)?”

노인, 신의가 쓰게 웃으며 고개를 끄덕였다.

“예, 맞습니다. 이 늙은이가 늦는 바람에 의도치 않게 결례를 범했군요.”

“아, 아닙니다! 결례라니, 당치 않습니다!”

호위장은 황급히 손을 내저으며 적천강의 눈치를 살폈다.

마침내 신의와 마주하게 된 것은 기쁜 일이었지만, 저 무시무시한 대머리 중년인의 정체에 비하면 아무것도 아니었다.

‘서, 설마.’

흐트러졌던 머릿속 조각들이 순식간에 짜 맞춰지는 듯한 기분이었다.

어림잡아도 칠순이 넘어 보이는 신의를 어린아이 취급하는 모습. 단순히 발산한 것만으로도 전신을 옥죄던 압도적인 기파.

아니, 정확히는 열양지기.

거기에 더해 마지막으로 조금 전 들었던 신의의 말까지.

‘적 대협이라고 했다. 분명히.’

호위장은 자신도 모르게 마른 침을 꿀꺽 삼켰다.

헛소리다. 미친 생각이다.

그러나 어쩔 수 없었다. 호위장이 알기로 이 모든 조건을 충족시킬 수 있는 사람은, 천하를 뒤집어 탈탈 털어도 한 사람뿐이었으니까.

“저, 저분은 혹시 화, 화, 화…….”

차마 말을 잇지 못하고 더듬거리는 호위장을 향해, 적천강이 눈살을 찌푸렸다.

“그래, 노부가 바로 화왕(火王)이니라. 화화화왕이 아니라.”

“히이익!”

“……이놈 반응이 왠지 기분 나쁜데. 저승사자라도 된 기분이군.”

도무지 이해할 수 없다는 듯한 적천강의 모습에, 신의는 문득 과거 스승에게 들었던 이야기를 떠올렸다.



‘무림인이란 족속들은 기본적으로 멀리하는 것이 상책이다.’

‘어째서입니까?’

‘세상에 존재하는 모든 인간군상 중에서 가장 비열하고, 난폭하며, 심지어 멍청하기까지 하니까.’

‘아, 어느 정도는 맞는 말 같군요.’

‘……무슨 뜻이냐?’

‘아무것도 아닙니다. 한데 제자는 모든 무림인이 그런 것은 아니라고 알고 있습니다만.’

‘사실이지. 하지만 사마외도(邪魔外道)만큼은 믿고 걸러야 한다. 백중 구십구가 병신이니.’

‘정파에는 뜻 있는 협객들이 있다고 들었습니다. 그들도 피해야 합니까?’

‘어지간하면 피해라. 입으로만 인의(人義)를 논할 뿐, 그중 절반은 병신이다.’

‘그렇다면 정파에도, 사마외도에도 속하지 않은 정사지간(正邪之間)의 무림인은 어떻습니까?’

‘그들은 워낙 제멋대로인 데다 알려지지 않은 이들이 많기에 판단하기 어렵다. 그러나 이 스승의 경험에 따르면, 넌 두 개만 기억하면 된다.’

‘그게 무엇입니까?’

‘화왕. 열화문. 따라 하며 머릿속에 새기거라.’

‘화왕. 열화문.’

‘한 번으로는 부족하다. 이번에는 마음에 새기며 말해라.’

‘화왕. 열화문.’

‘잘했다. 이 두 개만 기억하거라.’

‘화왕이라는 별호는 언뜻 들어본 것 같습니다만, 제자가 굳이 이렇게까지 기억해야 하는 이유가 무엇입니까?’

‘피해라.’

‘예?’

‘그 어떤 상황에서도 절대 마주치지 마라. 만약 내가 없을 때 어디선가 화왕이 나타났다는 소문이 들리면, 아예 그 성(省)을 떠야 한다.’

‘아니 무슨, 도대체 어떤 사람이기에 그렇게까지 해야 합니까?’

‘미친놈이다.’

‘……?’

‘화왕은, 아니 열화문은 대대로 정파와 사마외도를 가리지 않고 싸워 대는 미친놈들이다. 그냥 기분 나쁘면 패고, 기분 좋아서 패고, 어느 날은 기분이 좋지도 나쁘지도 않아서 팬다.’

‘……어찌 그런 이들이 있을 수 있습니까?’

‘있다. 자그마치 삼백여 년 동안이나 미치도록 강한 미친놈들을 대대로 싸질러, 아니 배출해 낸 미친 문파가.’



신의는 똑똑히 기억하고 있었다.

고금제일의 살수(殺手)로 불리는 만큼 언제나 냉정을 유지하던 자신의 스승이, 미친이라는 표현을 연달아 세 번이나 써 가며 위험을 강조했던 그 날을.

‘그런데 적 대협께서는 왜 억울해하실까. 전부 맞는 말 같은데.’

물론 그 생각을 입 밖에 내지는 않았다. 그보다는 호위장의 멱살을 붙잡고 윽박지르는 적천강을 말리는 것이 우선이었으니까.

“노부가 그렇게 흉악해 보이느냐? 어?”

“히익! 아, 아닙니다!”

“그런데 왜 목소리가 떨리느냐! 지금 노부가 대머리라 우롱하는 것이냐!”

“히이익! 그, 그런 적 없습니다! 제발 살려 주십시오!”

“한 번만 더 목소리를 떨었다간 네놈의 몸뚱어리에 존재하는 털이란 털은 싹 다……!”

“적 대협, 이제 그만 고정하시지요.”

한숨을 내쉬며 적천강을 말린 신의가 벌벌 떨고 있는 호위장에게 말했다.

“의도치 않게 대강의 사정은 들었습니다만, 본론부터 말씀드리자면 저는 자리를 뜰 수 없습니다.”

“예, 예? 아니, 어째서 그런!”

“호위장이 말씀하신 바에 의하면 성주께서는 그저 조금 특이한 상사병(相思病)을 앓고 계실 뿐입니다. 의원인 저로서는 더 아프고 고통받는 이들을 보살필 수밖에요.”

“하, 하지만 평소의 행실과 너무 다른 모습을 보이고 계시단 말입니다!”

“당연한 일입니다. 사랑하는 이를 빼앗겼으니 그 심정이야 오죽하겠습니까. 혹여 나중에라도 제가 맡은 환자들의 차도가 나아지면, 그때라도 한 번 들를 터이니…….”

순간 말꼬리를 흐린 신의의 고개가 살짝 열린 문틈을 향했다.

이 자리의 누구도 들을 수 있을 정도로 다급한 발걸음과, 거친 호흡이 가까워지고 있었다.

무림인에게서는 좀처럼 들을 수 없는, 갑옷 특유의 소음과 함께.

타다닥, 철컹!

아니나 다를까. 얼마 지나지 않아 번쩍이는 철갑(鐵甲)을 걸친 이가 달려와 문 앞에서 쓰러지듯 걸음을 멈췄다.

“넌…….”

성주부에 남아 있어야 할 수하의 얼굴을 확인한 호위장의 눈동자가 커진 그때. 거친 숨을 토해 낸 수하가 부르짖듯 외쳤다.

“서, 성주께서……!”
```

## Final English reading copy

```markdown
# Chapter 847

The world was vast.

Yet just as the two characters that made up *天下*—“all under Heaven”—suggested, there was Heaven above it all.

The wide earth and the seas. The living and the dead.

Nothing could hide from Heaven.

Even birds that flew with the clouds across the distant sky, even humans who ceaselessly rose and fell and pointed blades at one another, all looked up at Heaven.

Wondering what magnificent being might dwell up there.

That was what Heaven meant to people.

An unknown realm they could only gaze at, never reach. Something they feared and revered in equal measure.

So perhaps it was only natural that the one who possessed all under Heaven came to be called the Son of Heaven.

The blue sky that looked down on everything in the world was the ultimate symbol of authority, after all.

*But even the Son of Heaven is just a man in the end. Look at him—stealing another man’s favored concubine and all.*

The astonishment from a moment ago vanished, replaced by a quiet laugh.

At the sight of Jeok Cheongang chuckling, the Captain of the Guards looked awkward.

“It wasn’t exactly a funny story.”

“No? From where I’m sitting, it was plenty funny. The man they even call the Son of Heaven steals his subject’s favored concubine, and the poor subject gets lovesick enough to hover between life and death.”

“……!”

The Captain of the Guards was so shocked he forgot to breathe.

He’d already guessed the man was crazy, but to say something so disrespectful about the Son of Heaven—

He hurriedly checked for anyone nearby, then managed to squeeze out a voice.

“A-are you insane? I don’t know who you are, but how dare you say that about His Majesty the Emperor…!”

“What, are you scared?”

“Do you even have to ask? Good heavens, if anyone else had heard you, you’d be charged with treason on the spot.”

“Hm. Treason, you say.”

Jeok Cheongang scratched his chin as he considered it.

Maybe not in the past, but now he was a Master with a Disciple, and a member of the Murim Alliance to boot.

“That could make things a little awkward.”

“Awkward? Do you think treason is some petty offense?”

“It’s not a crime so great that it warrants wiping out all nine branches of a family. The Son of Heaven is still a person made of flesh and blood. What’s the big deal if he gets insulted a little?”

“……!”

“Your face is a sight to behold. Heh heh.”

The Captain of the Guards stood frozen with his mouth agape. Jeok Cheongang slapped his knee and laughed.

He had lived for a hundred and several dozen years.

He’d seen with his own eyes the age of warring heroes, when the blood never dried, and the birth of a new unified dynasty.

The Son of Heaven—an object of awe and reverence?

What a joke.

For as long as he could remember, the title had never meant all that much to Jeok Cheongang.

*Just someone a little more extraordinary than others, with far greater ambition and cruelty.*

That was Jeok Cheongang’s assessment. And after hearing his one and only Disciple’s stories, he was even more certain.

He’d judged it right.

The Son of Heaven wasn’t bestowed by Heaven. He was born amid countless rivers of blood and heaps of corpses.

Jeok Cheongang suddenly remembered the stories Jin Taekyung had told him: astonishing tales of a giant iron bird taking to the sky and traveling among countless stars.

As he thought of them and watched the Captain of the Guards still standing frozen, he couldn’t help letting out another laugh.

“I understand. There’s a mountain of things even this old man doesn’t know. How could a little sprout like you begin to imagine them?”

“Th-this old man? Little sprout?”

“The world is vast, and the years keep passing. Maybe Dongfang Shuo, who lived through three thousand jiazi, could have watched it all change.”[^1]

The Captain of the Guards stared at Jeok Cheongang, dazed.

The man looked about his age, yet spoke in such a strange way. And none of what he was saying made sense to him.

“What on earth does that—”

The Captain of the Guards trailed off.

“You don’t need to try to understand. Anyone listening to a story like that would have the same questions.”

“……!”

At the sudden voice that slipped into his ear, the Captain of the Guards sucked in a breath and instinctively drew the sword at his waist, swinging it.

Or he tried to.

Until a terrifyingly immense energy erupted from somewhere and pressed down on his entire body.

Whoosh!

A wave of qi, hot as flames and heavy as a mountain.

The Captain of the Guards froze, not daring even to breathe.

His head had bowed beneath the force pressing down on it. His eyes trembled with agitation as he stared at his hand, still short of the sword hilt.

*H-how?*

Only the unanswered question drifted through the Captain of the Guards’ mind, bleached white with shock.

How could this be?

He’d left Murim to join the government in search of a comfortable life, but he was still a Peak master.

And not some hothouse flower raised in the shelter of a prestigious sect. He was a Peak master who’d come up as a wandering martial artist, hardened by real combat.

He’d spent more than twenty years as a wanderer.

He’d gone to war as soon as his first downy hairs appeared, and survived by turning into a stubborn weed.

He might not have learned the fine martial arts taught to the disciples of great families, but he was proud that his experience on the brink of death surpassed theirs.

And yet…

*If I move, I die.*

He could see it clearly. Feel it plainly.

The shadow of death drawing near. A towering wall he could never overcome, even if he were reborn again and again.

Drip.

At that very moment, a bead of cold sweat that had formed without his noticing ran down from the Captain of the Guards’ chin.

“It’s a hot day. That’s a bit much to put a guest through.”

Ssshhh.

At the calm voice, the heat scattered as if it had never been there.

The Captain of the Guards let out the breath he’d been holding and took several ragged breaths. In his ears, the sound of a conversation reached him.

“A guest? He’s just some nobody here to make a request that isn’t even worth calling a request.”

“Technically, he’s my guest. He came to see me, after all.”

“What kind of guest tries to draw his sword the moment he arrives?”

“I understand. Anyone could do that if they were startled while still reeling from shock.”

“Quiet. You’d better be grateful to this old man for keeping you safe.”

“I can’t compare to you, Sir Jeok, but I did learn a thing or two from my Master. You needn’t worry.”

“No, but this brat who doesn’t even have the blood dried on his head has been talking back to me all this time—”

“As a physician, I’d point out that if the blood in your head dries up, you die.”

“You—!”

The Captain of the Guards, listening to them, lifted his head in confusion.

Far from being a child with wet blood still on his head, an old man with snow-white hair looked at him with kind eyes.

“Are you all right?”

“……!”

In that instant, the Captain of the Guards recognized the old man by instinct.

He had the bearing of an immortal. And the conversation he’d just overheard contained all the answers.

“D-Divine Physician?”

The old man—the Divine Physician—smiled wryly and nodded.

“Yes, that’s right. This old man was late, and I ended up offending you without meaning to.”

“N-no! You didn’t offend me at all!”

The Captain of the Guards hurriedly waved his hands, then glanced nervously at Jeok Cheongang.

Meeting the Divine Physician at last was wonderful, but it was nothing compared to finding out who that terrifying bald middle-aged man was.

*Could it be…?*

The scattered pieces in his mind seemed to fall into place all at once.

The way he treated the Divine Physician, who looked to be well past seventy, like a child. The overwhelming force that had bound his entire body with nothing more than its release.

No—more precisely, the Scorching Yang Qi.

And, finally, what the Divine Physician had just called him.

*He said “Sir Jeok.” He definitely did.*

The Captain of the Guards swallowed hard.

It was nonsense. A crazy thought.

But he couldn’t help it. As far as he knew, there was only one person in all the world who fit all those details.

“Th-that person, could he be F-F-Fire—”

The Captain of the Guards stammered, unable to finish. Jeok Cheongang frowned.

“That’s right. I am the Fire King. Not the F-F-Fire King.”

“Eek!”

“……His reaction is somehow getting on my nerves. I feel like the Grim Reaper.”

At Jeok Cheongang’s baffled look, the Divine Physician was reminded of something his Master had once told him.

> “As a rule, it’s best to keep your distance from martial artists.”
>
> “Why?”
>
> “Of all the kinds of people in the world, they’re the most vile, violent, and—on top of that—stupid.”
>
> “Ah, I suppose that’s true to some extent.”
>
> “……What do you mean by that?”
>
> “Nothing. But I thought not all martial artists were like that.”
>
> “True. But steer clear of those who follow the demonic, heterodox arts. Ninety-nine out of a hundred are idiots.”
>
> “I’ve heard there are righteous heroes among the orthodox faction. Should I avoid them, too?”
>
> “If you can, yes. They talk about benevolence and righteousness, but half of them are idiots.”
>
> “Then what about martial artists who belong to neither the orthodox faction nor the ranks of those who follow the demonic, heterodox arts?”
>
> “They’re so unruly, and so many of them are unknown, that it’s hard to judge. But based on my experience, you only need to remember two things.”
>
> “What are they?”
>
> “The Fire King. The Fire Gate Clan. Repeat them and burn them into your mind.”
>
> “The Fire King. The Fire Gate Clan.”
>
> “Once isn’t enough. This time, say them and engrave them on your heart.”
>
> “The Fire King. The Fire Gate Clan.”
>
> “Good. Remember those two.”
>
> “I think I’ve heard the title Fire King before, but why do I need to remember it so well?”
>
> “Avoid him.”
>
> “Pardon?”
>
> “Never meet him, no matter what. If you hear a rumor that the Fire King has appeared somewhere while I’m away, leave the entire province.”
>
> “What? What kind of person is he that I’d have to go that far?”
>
> “A lunatic.”
>
> “……?”
>
> “The Fire King—or rather, the Fire Gate Clan—are lunatics who’ve spent generations fighting orthodox martial artists and followers of the demonic, heterodox arts alike. They beat people when they’re in a bad mood, when they’re in a good mood, and some days when they’re neither happy nor upset.”
>
> “……How can people like that exist?”
>
> “They do. There’s a mad sect that’s spent more than three hundred years breeding—no, producing—one generation of insanely strong lunatics after another.”

The Divine Physician remembered that day clearly.

His Master, who always kept his composure and was known as the greatest assassin of all time, had stressed just how dangerous they were by using the word “lunatic” three times in a row.

*Then why does Sir Jeok look so offended? Everything he said sounds right.*

Of course, the Divine Physician didn’t say that out loud. He had more important things to do—like stop Jeok Cheongang, who had grabbed the Captain of the Guards by the collar and was now shouting at him.

“Do I look that vicious to you? Huh?”

“Eek! N-no!”

“Then why is your voice shaking? Are you mocking me for being bald?”

“Eek! I-I didn’t! Please spare me!”

“If your voice shakes one more time, every last hair on your body is going to…!”

“Sir Jeok, that’s enough. Please calm down.”

The Divine Physician sighed as he stopped Jeok Cheongang, then spoke to the trembling Captain of the Guards.

“I heard most of the situation without meaning to, but to get straight to the point, I can’t leave.”

“Y-yes? Why not?”

“From what you’ve told me, the City Lord is suffering from a rather unusual case of lovesickness. As a physician, I have no choice but to care for those who are sicker and in greater pain.”

“B-but his behavior is so different from usual!”

“That’s only natural. He’s had the person he loves taken from him. How could he not be suffering? If my patients improve later on, I’ll come by then, even if it’s only once…”

The Divine Physician’s voice trailed off. His gaze shifted toward the slightly open door.

A hurried footfall and ragged breathing were drawing closer, loud enough for everyone there to hear.

Along with the unmistakable clank of armor—a sound seldom heard from a martial artist.

Tap-tap-tap! Clank!

Sure enough, before long, a figure clad in gleaming armor ran up and came to a halt in front of the door, nearly collapsing.

“You…”

The Captain of the Guards’ eyes widened when he recognized a subordinate who should have been back at the City Lord’s residence. The man sucked in a ragged breath and cried out:

“C-City Lord…!”

[^1]: Dongfang Shuo is a figure in Chinese folklore associated with extraordinary longevity; a *jiazi* is a traditional sixty-year cycle.
```
