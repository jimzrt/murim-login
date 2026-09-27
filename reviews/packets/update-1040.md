<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1040.txt",
      "sha256": "3266582782d4dc671e7e4dc1bc79d634e207801442cc851f43d740b96ca4f248",
      "bytes": 13468
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d3410abe81c4bb42e70029c1fabfbdbf4cbd4fe5c8cf9cca413e54c4c06d805a",
      "bytes": 967
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "40afac2714a80a3a8ce8426a820354a73a3bfdd5d8ebd65cc23a9e6b25ecae22",
      "bytes": 240805
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "95898d50df4572bdf1845cc8f2bb7c0c16b01e45d6541d0e208d2e89a8bc3637",
      "bytes": 914
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "ac52a4650d79d156afc8039666b589d10f39cfdefe209430644c3bedcef1a4a1",
      "bytes": 760
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "5af2a8f43d86d40ef598f9a260c69d03a150cd073cf2b66d64371fdf50860839",
      "bytes": 1823
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "584c3f37db4de74617d6a808671e7c1a87010d1dd06267a2aefa11f4a1802f80",
      "bytes": 623
    },
    {
      "path": "characters/So Gunak.md",
      "sha256": "05f690607787cd210f46182b8aab3bb004ca63e697a21a86a40a766ce3305160",
      "bytes": 399
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "ed4a61c5e26441b036619799633835cb56305b1f512227194094b6a2a69aa9f9",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f78099b144ce0321743eec5fdf0c165083ec3e8ae3c8bf959eafb1b530843846",
      "bytes": 279561
    }
  ],
  "estimated_tokens": 10278
}
-->

# Durable State Update — Chapter 1040

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
1 and safe_through 1040. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1040. Profile updates may replace only one
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
  "chapter": 1040,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1040,
    "continuity_sources": [1040],
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
    "The Blood-Sword Demon Lord serves the Lord of Heaven and commands the invading army.",
    "Jeok Cheongang is injured but holding off the Blood-Sword Demon Lord while Jin Taekyung targets the mages.",
    "The mages’ Magic empowers the Blood-Sword Demon Lord and is increasing the strength of So Gunak and the other defenders.",
    "Jin Taekyung is fighting So Gunak, the last Black Ghost, and more than a hundred Peak masters to reach the mages.",
    "Jin Taekyung summoned Fire Dragon Armor as he charged into the defenders."
  ],
  "continuity_sources": [
    1038,
    1039
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who are the white-robed mages, and what is their purpose?",
    "How were the former Demonic Cult fiends made into Black Ghosts?"
  ],
  "safe_through": 1039,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 암천     | **Dark Heaven**                  |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 레벨               | **Level**                      |
| 마법사     | **mage**              |
| 귀가      | **your family**                                                 |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 소군악 | **So Gunak** | Name shown in the System status. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 여의주 | **dragon pearl** | Legendary treasure requested by Jang Taebo. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 신병이기 | **divine weapon** | Jin's description of White Flame. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 풍귀 | **Wind Ghost** | Power invoked by a white-robed figure and imbued in the Blood-Sword Demon Lord. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 혈검마군 | 진태경 | enemy addressing a younger martial artist | you | familiar and measured | Uses 자네 while praising and assessing Taekyung. |
| 진태경 | 혈검마군 | young martial artist confronting an enemy | you | casual and challenging | Questions when the Blood-Sword Demon Lord and the Lord of Heaven appeared. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1039
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Devoted to his master and proud of his abilities, he is deeply wounded by perceived distrust and resolves to prove his worth.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He serves the Lord of Heaven with deep devotion but believes his master does not fully trust him; he has been ordered not to kill Jin Taekyung, admires Jeok Cheongang, and once shared the Demonic Cult with the fiends who became Black Ghosts.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1039
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1039
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Taekyung trusts Sama Pyo and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1039
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### So Gunak.md

# So Gunak (소군악)

- **Safe through:** Chapter 1039
- **Aliases:** None
- **Role:** So Gunak is a Black Ghost, a former Demonic Cult fiend transformed into a black-armored warrior.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He is one of the Blood-Sword Demon Lord’s Black Ghosts.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1039
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1040화



콰아아아앙!

무시무시한 폭음과 함께 지축이 뒤흔들린다.

부지불식간에 터져 나와 온 사방을 떨어 울린 그 거대한 진동은, 반경 수십여 장을 넘어 가파른 언덕 위까지 전해지기에 충분했다.

드드득.

“속하가 한 말씀 드려도 되겠습니까?”

지면의 떨림과 함께 귓가를 파고든 노쇠한 목소리에, 은백색의 면사 아래로 붉은 입술이 달싹였다.

“아니, 안 돼.”

불과 일각 전, 혈검마군의 분노에 당황했던 여인의 모습은 조금도 찾아볼 수 없다.

담담한 것을 넘어 냉정하게까지 느껴지는 상관의 대답에, 늙은 술사의 신형이 움찔 떨렸다.

“……대술사(大術師)시여.”

근심이 가득 담긴 음성.

그러나 대술사라 불린 여인, 백의인들의 중심에 선 그녀는 아랑곳하지 않고 입을 열었다.

“괜한 우려는 넣어 둬. 당신이 우려하는 상황은 일어나지 않을 테니까.”

“하, 하지만.”

“하지만, 뭐?”

평소였다면 수하인 늙은 술사도 이쯤에서 입을 다물었을 것이다.

암천 내부의 상하 관계는 잔인하리만치 철저했고, 눈앞의 여인에게는 그를 간단한 손짓 한 번으로 개미처럼 짓눌러 죽일 만한 힘이 있었으니까.

하지만 늙은 술사는 똑똑히 보았다.

마지막 순간, 무수한 섬광에 뒤덮이던 한 사람의 모습을.

무모한 정도를 넘어, 이미 삶을 포기한 것처럼 예정된 죽음 앞에 스스로 몸을 내던졌던 청년의 모습을.

그렇기에 스스로의 역할을 잘 알고 있는 늙은 술사는, 마른침을 꿀꺽 삼키며 어렵사리 말을 이어 갈 수밖에 없었다.

“허나 이대로라면 위험할지도 모릅니다. 대술사께서도 아시다시피, ‘그’가 이곳에서 죽어 버린다면 그분의 진노를 어찌 감당하오리까.”

맞다.

열화신룡(烈火神龍) 진태경.

절대자의 지대한 관심을 한 몸에 받는 그가 이토록 허망한 죽음을 맞이한다면, 자신들 역시 임무를 실패한 대가로 죽을 것이다.

아니, 죽는다. 틀림없이.

설령 그것이 눈앞의 여인, 자신의 상관이자 절대자의 최측근 중 하나인 대술사라 해도 예외는 아닐 것이라고 늙은 술사는 생각했다.

물론, 그 혼자만의 생각일 뿐이었지만.

“위험? 죽어?”

수하가 건넨 말을 뇌까린 여인은 문득 실소를 흘렸다.

촘촘하게 짜인 면사 너머, 까맣게 빛나는 눈동자는 줄곧 그래왔듯이 언덕 아래를 응시하고 있었다.

“도대체 누가?”

“예? 그야 당연히…….”

반사적으로 되물은 늙은 술사가 말을 이으려던 그 순간.

화아아악.

언덕 밑을 뒤덮은 희뿌연 먼지구름이 좌우로 갈라졌다.

그리고 마치 보이지 않는 예리한 칼날이 스쳐 지나간 것처럼, 선명하게 분리되는 장막 너머로 숨겨져 있던 광경이 드러났다.

“……!”

“……!”

늙은 술사가, 아니 언덕 위의 모두가 눈을 부릅떴다.

지금 이 순간 경악으로 물든 그들의 눈동자에 비친 것은, 유성이 떨어진 것처럼 초토화된 지면을 딛고 우뚝 서 있는 어떤 존재였다.

“저, 저건.”

어느 한 술사가 자신도 모르게 손을 들어 가리켰지만, 이러한 행동이 무색하게도 이미 주위의 모든 시선은 그쪽을 향해 있었다.

누구라도 올려다볼 수밖에 없을 구척장신의 거구와 기둥처럼 굵은 팔과 다리.

그리고 그런 전신을 빈틈없이 감싼 검은색의 갑주를 걸친 낯익은 존재를.

“흑귀……!”

늙은 술사의 입술 사이로 파르르 떨리는 침음성이 흘러나왔다.

찰나의 경악이 사라지고, 짙은 절망감이 차지한 그의 눈동자는 피투성이가 된 채 흑귀의 발치에 쓰러져 있는 한 사람을 향하고 있었다.

이곳에서 죽어서는 안 되는 그, 바로 진태경을.

‘끝장이다. 전부 다.’

늙은 술사는 순간 아득해지는 시야를 느꼈다.

앞서 조금 전, 대술사가 보인 모습에 일말의 희망을 가졌던 그였기에 충격은 더욱 컸다.

혹시 모를 상황을 대비해 호위로 남겨 놓은 일백의 최정예들이 절반이나 증발해 버렸지만, 진태경이 죽었다는 사실에 비하면 아무것도 아니었다.

비단 그 혼자뿐만이 아니라, 스무 명의 술사들 모두가 그렇게 생각하고 있었다.

적어도 바로 다음 순간, 대술사의 나직한 음성이 울려 퍼지기 전까지는.

“역시…….”

도무지 의미를 알 수 없는 뇌까림. 그 안에 담긴 경탄의 감정을 느낀 술사들은 눈을 크게 떴다.

그리고 동시에, 볼 수 있었다.

스륵, 쿵.

저 멀리, 언덕 아래에서 썩은 통나무처럼 허물어지는 흑귀의 신형을.

조금 전까지 그 거대한 몸뚱어리에 가려져 보이지 않았던, 흑귀의 미간 사이에 틀어박힌 은빛 창날을.

하지만 그들은 보았되, 결코 들을 수 없었다.

띠링.

오직 한 사람에게만 허락된 그 맑은 종소리를.

모두가 죽었다고 믿었던, 그러나 아직 죽지 않았던 그의 귓가에 울려 퍼진 회생(回生)의 목소리를.



- [Lv.175 소군악]을 처치하셨습니다!

- 레벨 업!



스아아아.

따스한 온기를 머금은 광휘가, 차갑게 식어 가던 몸속 깊은 곳으로부터 솟아올랐다.

무수한 검기과 강기에 의해 파괴된 붉은 갑옷 틈새로 흘러나오던 피를 멈추고, 갈라진 살과 뼈를 잇고, 그렇게 다시 한번 생명의 불씨를 피워 올렸다.

후우.

불꽃처럼 뜨거운 숨결.

긴 꿈에서 깨어난 듯, 천천히 눈을 뜬 진태경은 다시 한번 마주하게 된 어두운 하늘을 바라보며 중얼거렸다.

“시벌, 존나게 반갑다.”

그리고 그 믿지 못할 광경을 본 순간, 늙은 술사는 깨달았다.



‘위험? 죽어?’



조금 전 들었던 말의 의미를.



‘도대체 누가?’



대술사의 반문이 옳았다.

이제 죽음의 위험을 감수해야 하는 것은 진태경이 아니라, 바로 그들 자신이었으니.

쉬릭, 덥석.

흑귀의 미간 깊숙이 박혀 있던 한 자루의 창이 보이지 않는 힘에 이끌리듯 주인의 손아귀로 빨려 들어간다.

아니, 그랬다고 느낀 순간 섬광이 되어 쏘아졌다.

쐐애애액, 퍼걱!

거대한 용의 꼬리처럼 맹렬하게 휘둘려져, 살아남은 적들을 도륙해 나가는 검푸른 불길.

“대술사시여!”

“모든 수를 동원해서라도 막아야 합니다! 이대로라면 놈이, 놈이……!”

늙은 술사를 시작으로 곳곳에서 터져 나오는 다급한 외침.

하지만 그 끔찍하고도 경이로운 광경을 말없이 응시하고 있는 대술사의 눈빛은, 알 수 없는 이채로 번뜩이고 있었다.

‘드디어.’

혀끝에서 맴도는 나지막한 탄성.

이내 명령을 기다리지 못한 술사들이 이를 악물며 앞으로 나선 그때에도, 그녀는 홀로 조용히 웃고 있었다.



* * *



무림에서 처음 눈을 떴던 그 순간부터, 내가 수없이 맞닥트린 현실을 간단히 정의하자면 이렇다.

하이 리스크(High Risk), 하이 리턴(High Return).

항상 그랬다.

결말이 정해지지 않은 모험은 언제나 크나큰 위험을 동반하지만, 위험한 만큼 돌아오는 대가는 확실했다.

바로 지금처럼.

띠링. 띠링. 띠링. 삐비빅.

연달아 울려 퍼지는 종소리와 경고음이 귓가에서 뒤섞인다.

마지막 장애물이었던 흑귀를 처치했다는 메시지와 레벨 업, 그 효과로 말미암아 회복했음을 알리는 홀로그램 창.

그리고 마지막 경고음의 정체는…….



- [화룡갑]이 강력한 기운에 의해 극심한 손상을 입었습니다!

- [화룡갑]이 [인벤토리]로 자동 소환됩니다! 파손 부위를 일정 수치까지 수복하기 전까지는 재소환할 수 없습니다!

- [화룡갑]의 자동 수복까지 남은 시간 : 3일



내가 모험을 시도할 수 있었던 가장 큰 이유이자, 이런 미친 짓을 벌였음에도 잠시나마 죽음을 늦춰 주었던 신병이기(神兵利器)의 희생을 알리는 내용이다.

‘이걸 사네.’

죽음의 끝자락에서 겨우 회생했기 때문일까.

아직도 잘 실감이 나지 않는다.

물론 당연히 살 수 있으리라는 희망을 안고 던진 도박수인 것은 맞다.

단지 백 퍼센트의 확신까지는 없었을 뿐이지.

아마도 저 빌어먹을 흑귀가 조금만 더 늦게 숨이 끊어졌다면, 기껏해야 동귀어진(同歸於盡)으로 끝났을 것이다.

하지만…….

서걱!

나는 살아 있다. 살아남았다.

처음부터 지금까지 늘 그래 왔듯이. 이곳에 남아 끊임없이 적들을 쓰러트리고 있었다.

목숨을 건 모험의 대가로 얻어 낸, 활력이 넘치는 이 몸뚱어리로.

푸푹, 펑!

힘차게 내뻗어 낸 창날로 세 명의 적을 단숨에 꿰뚫고, 그 틈을 노려 사각에서 달려드는 적들에게는 일장(一掌)을 흩뿌렸다.

콰아아아!

끔찍한 열기로 인해 녹아내리는 살과 뼈.

조금 전 있었던 흑귀와의 격돌 직후 살아남은 오십여 명의 적들은, 이 순간에도 눈에 띌 만큼 줄어들고 있었다.

‘더 빠르게, 더, 더.’

그러나 나는 이를 악물며 더욱 힘을 가했다.

한순간이라도 신속하게 이 전투를 끝내야 했다.

이미 극한까지 다다른 정신력은 바닥을 드러낸 상황.

레벨 업으로 회복된 몸뚱어리가 아니었다면, 아직 등 뒤에 남아 있는 이들을 생각하지 않았다면 진즉 쓰러졌을지도 모른다.

‘놈들은 쓰러트리기 전까지, 결코 쓰러지지 않는다.’

나는 홀린 듯이 백염을 휘둘렀다.

어느덧 중단전의 이능(異能)을 한계까지 쏟아부은 대가로 확연히 느려진 두뇌보다, 끊임없는 훈련과 본능으로 움직임이 각인된 손발이 적들을 휩쓸고 있었다.

이성보다는 본능에 몸을 맡긴 상황.

이런 와중에도 끈질기게 부여잡고 있는 마지막 이성의 끈이 있다면, 그것은 내가 쓰러지지 말아야 할 이유와 적들이 가진 가장 큰 변수였다.

‘마법.’

아마도 그 덕분이었을 것이다.

이성을 앞질러 그 어느 때보다 날카로워진 본능이, 줄곧 마음속에 품고 있던 그 두 글자에 대한 경계심이 또 한 번의 이변(異變)을 감지해 낸 것은.

우우웅.

공간이, 대기가 흔들린다.

그리고 그와 동시에, 저 멀리 다급한 외침이 터져 나왔다.

“풍귀(風鬼)의 힘이여!”

“역발산(力拔山)의 기세여!”

화아악!

언덕 위에서 들끓어 오른 기운이 이곳을 향해 치달았다.

주문과 함께 이루어진 발현(發現).

하지만 나는 안다.

이런 종류의 신체 강화 마법은, 결국 그 대상이 살아 있어야 발동된다는 것을.

슈확!

검푸른 불길로 뒤덮인 백염의 창날이 공기를 찢었다.

그 무시무시한 불의 고리가 그리는 궤적에는, 마법의 범위에 포함되어 있던 십여 명의 적들이 있었다.

스걱! 푹!

열 개의 목이 허공으로 솟구친 바로 그 순간, 옆구리를 타고 전해지는 격통.

그러나 이미 각오하고 있던 나는 아랑곳하지 않고 돌아서며 팔꿈치를 휘둘렀다.

우직! 콰아앙!

안면이 짓뭉개진 적의 신형이 튕겨나간다. 옆구리를 깊숙이 파고든 단검을 뽑아든 나는 섬광처럼 팔을 흩뿌렸다.

쉭, 푹!

둔탁한 소음과 함께 또 다른 적의 얼굴이 뒤로 젖혀졌다. 남아 있는 적은 이제 스물 남짓.

“이게 무슨……!”

“안 돼! 놈을 막아라!”

이제는 두려움마저 담긴 백의인, 아니 마법사들의 외침을 들으며 나는 어렴풋이 짐작할 수 있었다.

놈들이 사용할 수 있는 마법에는 한계가 있다고.

그것이 내가 아는 현대의 마법사들과 놈들의 차이라고.

그리고 다음 순간 그 확신이 불러온 자신감이, 고스란히 발끝에 실려 터져 나왔다.

으드득, 쾅!

땅거죽이 뒤집히고, 이내 녹아내린다.

염화일로(炎火一路).

한순간의 폭발과 함께 쏘아지는 내 신형을 막아설 수 있는 적은 이제 주위에 아무도 없었다.

제아무리 강하게 키운 사냥개라 한들 늑대를 대적할 수 없고, 천년 묵은 이무기라 한들 여의주 없이는 하늘로 올라갈 수 없는 것처럼.

설령 나를 막아서려는 것이, 사람이 아닌 무언가라 할지라도.

“태산(太山)이여.”

우우우웅.

“떨어트리고, 짓눌러라.”

기억에 남아 있는 목소리와 함께, 한 줄기 불꽃이 되어 쏘아지는 나를 향해 떨어져 내리는 거대한 중압감.

그러나 그때와는 달리, 나는 준비되어 있었다.

‘보인다.’

동시에 느껴진다.

기의 흐름이. 이 거대한 힘에 가려진 한 줄기의 선이.

그리고…….

‘지금.’

서걱!

소리조차 없이 공간을 가로지른 창날이, 태산을 베었다.
```

## Final English reading copy

```markdown
# Chapter 1040

KWA-BOOOOM!

A terrifying explosion shook the very earth.

The immense shock wave erupted without warning, rattling everything around it. It was powerful enough to reach beyond a radius of several dozen *jang* and all the way up to the steep hill.

Rumble.

“May I speak, my Lady?”

At the old man’s voice, which cut through the rumbling ground and pierced her ears, red lips stirred beneath a silver-white veil.

“No. You may not.”

There was no trace left of the woman who’d been rattled by the Blood-Sword Demon Lord’s fury just fifteen minutes ago.

At her superior’s cool, almost icy reply, the old mage’s frame twitched.

“…Grand Mage.”

His voice was filled with concern.

But the woman called the Grand Mage, standing at the center of the white-robed figures, paid him no mind as she spoke.

“Put your pointless worries aside. What you’re afraid of won’t happen.”

“B-but…”

“But what?”

Under normal circumstances, the old mage, her subordinate, would have fallen silent by now.

The hierarchy within Dark Heaven was mercilessly strict, and the woman before him had enough power to crush him like an ant with a mere flick of her hand.

But the old mage had seen it clearly.

At the last moment, one man’s figure had been swallowed by countless flashes of light.

A young man who’d thrown himself in front of what should have been certain death—not merely recklessly, but as if he’d already given up on living.

The old mage knew his own role well. Swallowing hard, he had no choice but to force the words out.

“But if things continue like this, he may be in danger. As you know, if ‘he’ dies here, how are we to bear that person’s wrath?”

He was right.

Jin Taekyung, the Blazing Flame Divine Dragon.

If the absolute one’s keenly watched favorite met such a futile end, they too would die for failing their mission.

No—they would die. Without a doubt.

The old mage believed there would be no exception, not even for the woman before him, his superior and one of the absolute one’s closest confidantes.

Of course, that was only what he thought.

“Danger? Die?”

The woman repeated his words, then let out a quiet laugh.

Beyond the finely woven veil, her black eyes remained fixed on the hill below, as they always had.

“Who, exactly?”

“Pardon? Why, of course…”

The old mage had just begun to answer when—

FWOOSH.

The hazy dust cloud covering the foot of the hill split apart.

And, as if an invisible, razor-sharp blade had passed through it, the veil parted cleanly to reveal the scene hidden within.

“……!”

“……!”

The old mage—and everyone on the hill—stared wide-eyed.

What their stunned eyes saw in that moment was a figure standing tall amid ground devastated as if by a falling meteor.

“Th-that’s…”

One mage raised a hand and pointed before he even realized what he was doing. The gesture was pointless; every eye nearby had already turned that way.

A familiar figure, towering nine feet tall, with arms and legs as thick as pillars.

His entire body was covered in black armor.

“Black Ghost…!”

A trembling groan escaped the old mage’s lips.

The brief shock vanished, replaced by deep despair. His eyes fixed on the man lying bloodied at the Black Ghost’s feet.

The one who must not die here.

Jin Taekyung.

*It’s over. All of it.*

The old mage’s vision blurred.

He’d held on to a sliver of hope after seeing the Grand Mage’s confidence just moments ago. That only made the shock worse.

Half of the hundred elite guards they’d kept behind in case of trouble had vanished. But compared to the fact that Jin Taekyung was dead, that meant nothing.

The twenty mages all thought the same.

At least, until the Grand Mage’s quiet voice rang out the very next moment.

“As expected…”

The mages widened their eyes at the incomprehensible murmur—and at the admiration in it.

Then, all at once, they saw.

Rustle. THUD.

Far below, the Black Ghost crumpled like a rotten log.

Only now could they see what had been hidden behind his enormous body: a silver spearhead embedded between his brows.

But though they saw it, they could not hear—

Ding.

The clear chime meant for only one person.

The voice of recovery sounded by the ear of a man everyone believed was dead, but who still lived.

> **System**
> - You defeated Lv. 175 So Gunak!
> - Level Up!

A warm radiance welled up from deep within his body, which had been growing cold.

It stopped the blood seeping through gaps in his red armor, torn apart by countless blades of Sword Energy and Force. It mended his torn flesh and broken bones, and rekindled the flame of life once more.

*Huff.*

His breath was hot as fire.

As if waking from a long dream, Jin Taekyung slowly opened his eyes. He looked up at the dark sky he’d seen once before and muttered,

“Fuck, it’s good to see you.”

The moment the old mage saw that unbelievable sight, he understood.

*Danger? Die?*

He understood what the words he’d heard a moment ago meant.

*Who, exactly?*

The Grand Mage had been right.

It wasn’t Jin Taekyung who now had to face the danger of death. It was them.

WHIP—GRAB.

The spear embedded deep between the Black Ghost’s brows flew into its owner’s grasp, as if drawn by an invisible force.

No—at the very instant it seemed to, it shot out in a flash.

SHWAAAAK—SPLAT!

A blue-black flame, swinging savagely like a giant dragon’s tail, tore through the surviving enemies.

“Grand Mage!”

“We have to stop him, whatever it takes! If this goes on, he’ll—he’ll…”

Urgent shouts rang out from all directions, starting with the old mage.

But the Grand Mage silently watched the horrifying, wondrous sight, her eyes flashing with an inscrutable light.

*At last.*

A quiet exclamation hovered on her tongue.

Even as the mages clenched their teeth and stepped forward, unable to wait for her command, she alone stood there, smiling quietly.

* * *

From the moment I first opened my eyes in Murim, I’d run into the same reality over and over. Put simply:

High risk, high return.

It had always been that way.

An adventure with no set ending always came with enormous danger. But the greater the risk, the more certain the reward.

Just like now.

Ding. Ding. Ding. BEEP-BEEP.

Chimes and warning beeps rang out in rapid succession, tangling together in my ears.

A message confirming I’d defeated the Black Ghost, the last obstacle. A Level Up. And a holographic window telling me I’d recovered as a result.

And the final warning beep was…

> **System**
> - Fire Dragon Armor has suffered severe damage from powerful energy!
> - Fire Dragon Armor has been automatically recalled to Inventory! It cannot be resummoned until the damaged sections are repaired to a certain degree!
> - Time until Fire Dragon Armor is automatically repaired: 3 days

The message told me my divine weapon had taken the hit. It was the biggest reason I’d been able to take this risk—and the thing that had kept death at bay, if only for a little while, despite the crazy stunt I’d pulled.

*I actually survived.*

Maybe it was because I’d just barely come back from the brink of death.

It still didn’t feel real.

Of course, I’d taken the gamble hoping I’d survive.

I just hadn’t been a hundred percent sure.

If that damned Black Ghost had taken even a little longer to die, we probably would’ve ended up killing each other at best.

But…

SHK!

I was alive. I’d survived.

Just as I had all along, from the very beginning, I remained here, relentlessly cutting down my enemies.

My body was brimming with life—the reward I’d won for risking my life.

PUK! BOOM!

I drove my spear through three enemies in one powerful thrust, then swept out a palm at those rushing in from my blind spot.

KWA-AAAA!

Flesh and bone melted in the terrible heat.

Of the fifty or so enemies left alive after my clash with the Black Ghost, their numbers kept visibly dwindling.

*Faster. Faster.*

But I gritted my teeth and pushed myself harder.

I had to end this fight as quickly as I could.

My mental strength, already stretched to the limit, was running dry.

If I hadn’t gotten my body back through the Level Up—if I hadn’t been thinking of everyone still behind me—I might have collapsed already.

*They won’t go down until I take them down.*

As if possessed, I swung White Flame.

My hands and feet, their movements etched into them through endless training and instinct, swept through my enemies faster than my mind could keep up. My brain had slowed sharply from pushing the Middle Dantian’s ability to its limit.

I was relying on instinct rather than reason.

Even so, there was one last thread of reason I clung to: the reason I couldn’t fall, and the greatest variable my enemies had.

*Magic.*

That was probably why.

My instincts, sharper than ever and racing ahead of my reason, sensed another anomaly. I’d been keeping those two words in the back of my mind all along.

WHOOOOOM.

Space and air trembled.

At the same time, a desperate shout rang out in the distance.

“The power of the Wind Ghost!”

“The might to uproot mountains!”

FWOOSH!

Energy boiled up from the hilltop and hurtled toward me.

An invocation, followed by its manifestation.

But I knew.

Magic that strengthened the body like this required its target to still be alive.

SHWAK!

White Flame, wreathed in blue-black fire, tore through the air.

The terrifying ring of fire swept through a dozen or so enemies within the spell’s range.

SHK! PUK!

Ten heads flew into the air.

At that very instant, pain flared along my side.

But I’d been ready for it. I turned without a second thought and swung my elbow.

CRACK! KWA-BOOM!

The enemy’s face caved in, and he went flying. I pulled the dagger from my side and swept out my arm in a flash.

SWISH—PUK!

With a dull thud, another enemy’s head snapped back. There were only about twenty left now.

“What is this…!”

“No! Stop him!”

Listening to the shouts of the white-robed figures—or rather, the mages—now tinged with fear, I could roughly guess what was happening.

There was a limit to the Magic they could use.

That was what set them apart from the mages I knew in the modern world.

And in the next moment, the confidence that certainty gave me burst out through my feet.

CRUNCH—BOOM!

The earth’s crust heaved, then melted away.

Flamefire Path.

With a single explosive burst, my body shot forward. There was no one left nearby who could stop me.

No matter how fiercely a hunting dog was raised, it couldn’t stand against a wolf. And even a thousand-year-old *imugi* couldn’t ascend to the heavens without a dragon pearl.

Even if the thing trying to stop me wasn’t human.

“Great mountain.”

WHOOOOOM.

“Fall and crush him.”

Along with a voice I remembered, an immense pressure bore down on me as I shot forward like a streak of flame.

But unlike last time, I was ready.

*I can see it.*

I could feel it, too.

The flow of qi. A single line hidden beneath that immense power.

And…

*Now.*

SHK!

My spearhead cut through space without a sound.

It cut through the great mountain.
```
