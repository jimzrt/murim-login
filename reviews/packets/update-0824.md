<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0824.txt",
      "sha256": "b088d6df218a2a73becefca76eb7c790d46c1dcbd4f599427fbe8d760c764113",
      "bytes": 12973
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2c446a428a5249cf1f78ae9a9aac131e889bfb0c6d50596eccc0863d25239704",
      "bytes": 1876
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3aa845c898a4d7baa3b82163a8c21152b9cc8866113c3b3793c09c7a03e2878f",
      "bytes": 226544
    },
    {
      "path": "characters/Amir.md",
      "sha256": "5ca782acf5bb79d3e10d4115869119a38a23cd217b9a8ea4a697c23caec184d5",
      "bytes": 575
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "cf0314ec458d40f304c9e4760d7cc6806d6fa6b2d719e6527b86c33823873695",
      "bytes": 723
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "4df1efa2dfff26075afbb32421195a498a004646033bd1dfa695a15882926efc",
      "bytes": 831
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "3576839dfba303354b914301859d8e5a52a80bb2e9f6030081767fb949039ae0",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "4f1576771481328e739b81376a60c1cd0c4a187f347caadbdcbde3101c9c540d",
      "bytes": 1853
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "5e93f66f7989c82b682a6e275f197674f3af86a59d5588f57af38b340358cffa",
      "bytes": 622
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "7f2f1c3048a4016e8c6620937b40df6f09777954608856d40aa0cc4a8a1dd06c",
      "bytes": 724
    },
    {
      "path": "characters/Yamamoto.md",
      "sha256": "e2cf19075619e6cc86b8fe0b2505c237635593ddecfd22a7d4335b7426475d9e",
      "bytes": 750
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d6eb10505e3ae21e2634e74e87280a075a9e5c9524aeeb977b2ad32b3670e66a",
      "bytes": 250419
    }
  ],
  "estimated_tokens": 10111
}
-->

# Durable State Update — Chapter 824

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
1 and safe_through 824. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 824. Profile updates may replace only one
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
  "chapter": 824,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 824,
    "continuity_sources": [824],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” who concealed itself for decades, including under the name Muninn.",
    "The Doppelganger can resurrect by consuming absorbed lives and reproduce absorbed people’s appearances, abilities, and memories; it has taken Siegfried Bassman’s face and Grand Mage abilities.",
    "The Doppelganger’s absorbed lives are dwindling; its left arm was torn off, and regeneration is slow after forcing Blink beyond its normal range.",
    "The Doppelganger fled west after the battle in the Rub’ al Khali Desert; Jin intends to stop its plan, which it has spent more than thirty years building.",
    "Jin defeated Hamid Shah Masoud and ended the battle against the fanatics, but his Middle Dantian is at its limit and his mental strength is depleted.",
    "Jin and the Skeleton King are about to pursue the Doppelganger by Teleport; Magic Johnson agreed to send them and stay behind to guard the battlefield."
  ],
  "continuity_sources": [
    822,
    823
  ],
  "open_questions": [
    "Who is the Doppelganger’s master, what is the plan, and why must the target be avoided until it is complete?",
    "What does the Chosen One designation mean?",
    "Will Jin and the Skeleton King reach the Doppelganger and stop it?",
    "Is Magic Johnson human?"
  ],
  "safe_through": 823,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 제자     | **Disciple**                                 |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 아미르 | **Amir** | Title used to address the group’s leader. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 야마모토 | **Yamamoto** | Japanese S-rank Hunter named in post-Leviathan media coverage. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 성지 | **Sacred Land** | Former name of the Poisonblood Grounds when beasts ruled Ailao Mountain. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 진태경 | 야마모토 | Alliance Leader to Japanese S-rank Hunter he sent on the mission | Yamamoto | blunt and familiar | Jin quietly says Yamamoto’s name while treating him. |
| 야마모토 | 진태경 | Japanese Hunter to the Alliance Leader who rescued him | Chōsenjin | insulting | Yamamoto uses the ethnic slur as he regains the ability to speak. |
| 진태경 | 선지자 | enemy commander addressed by Jin | The Prophet | blunt and informal | Jin asks where The Prophet is while confronting the Manticore Lord. |
| 진태경 | 도플갱어 | enemy | you; the Doppelganger | blunt and informal | Jin directly challenges the Doppelganger and demands to know what it wants. |
| 선지자 | 아미르 | religious leader to subordinate | Amir | authoritative | The Prophet addresses Amir by name and orders him to hold back Jin and the other heretics. |
| 아미르 | 선지자 | devotee to religious leader | Prophet | formal and deferential | Amir kneels and addresses the Prophet with reverence. |
| 진태경 | 아미르 | enemy commander | old man | blunt and insulting | Jin tells Amir to die, addressing him as 늙은이. |

## Listed compact profiles

### Amir.md

# Amir (아미르)

- **Safe through:** Chapter 822
- **Aliases:** None
- **Role:** Amir was the fanatics’ warrior chief and commander-in-chief, regarded by them as a warrior favored by God.
- **Personality:** Faithful and duty-bound, he advances alone against Jin despite the danger and questions his faith only as he faces death.
- **Voice:** Not established
- **Relationships:** The fanatics looked to Amir as their military leader and warrior chief, while The Prophet served as their spiritual leader.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 822
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 823
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger is a powerful being from the Demon Realm that spent decades manipulating events in the human world.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** Not established
- **Relationships:** It served an unnamed master who sent it to this world and ordered it to avoid the target until the master’s plan was complete; it regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 823
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 823
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 823
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 823
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” who concealed itself for decades as Muninn.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors and is revered by its followers; it made a pact with Michael Silbert during the 2020 Battle of Paris, where Michael killed the surviving humans in exchange for being spared.

### Yamamoto.md

# Yamamoto (야마모토)

- **Safe through:** Chapter 814
- **Aliases:** None
- **Role:** Yamamoto Genji was a Japanese S-rank Hunter assigned to J1; The Prophet later used his Level 120 identity until Jin destroyed that form.
- **Personality:** As The Prophet's Yamamoto Genji identity, he appeared prideful and easily offended, boasting of his rank but acting cowardly and evasive when danger became real.
- **Voice:** Not established.
- **Relationships:** As the Yamamoto Genji identity, he served with J1; Jin reprimanded and treated him after the attack, though Jin resented his late arrival during the Leviathan crisis.

## Korean source

```text
＃824화



새벽이 찾아오면, 어둠이 물러간다.

그것은 물이 위에서 아래로 흐르는 것처럼 당연한 이치 중 하나였지만, 누군가의 추격을 피해 도망치는 이들에게는 그리 달갑지 않은 소식이었다.

특히, 그 추격자가 인간인지조차 의심될 정도의 괴물이라면 더더욱.

‘벌써?’

도플갱어는 서서히 밝아 오는 하늘을 바라보며 입술을 깨물었다.

너무 이르다. 아니, 생각 이상으로 시간을 지체했다는 표현이 옳을 것이다.

‘최소한 날이 밝기 전에 모든 것이 끝났어야 했다.’

도플갱어도 알고 있었다. 아무리 후회하고 곱씹어 봤자 현실이 달라지지는 않는다는 것을.

그만큼 그가 세워 놓았던 계획은 이미 한참 전에 어그러졌고, 모든 것의 중심이자 시작에는 바로 ‘그놈’이 있었다.

‘진태경.’

욱신.

단지 이름을 떠올리는 것만으로도 몸 곳곳에서 찌르는 듯한 통증이 올라온다.

진태경에 의해 수백 번도 넘는 죽음을 겪은 도플갱어는 그 무시무시한 신위를 떠올리며 몸서리쳤다.

‘처음부터 놈에게 접근하지 말았어야 했다.’

실수였고, 욕심이었다.

야마모토 겐지를 흡수한 뒤 서둘러 자리를 뜨거나, 애초에 끝까지 모습을 드러내지 말았어야 했다.

‘조금만, 아주 조금만 더 채우면 되는 일이었는데.’

처음부터 목표는 다른 인간들이었다.

후방에 남겨져 있던 수많은 헌터들. 그들의 마나와 생명력을 흡수할 수 있다면, 소기의 목적을 달성할 수 있었으리라.

‘빌어먹을.’

하지만 진태경은 도플갱어를 쉽게 놔주지 않았다.

마치 노예를 부리듯이 그를 다루며 자신의 시야에서 벗어나는 것을 허락하는 법이 없었다.

그것은 도플갱어에게 있어 불행이었고, 진태경을 제외한 다른 헌터들에게는 행운이었다.

만약 도플갱어가 진태경의 손아귀를 벗어났다면, 야마모토 겐지의 거죽을 덮어쓰고 후방의 본대로 향했다면…… 수많은 몬스터와 광신도들을 이끌고 사막을 피로 물들였을 테니까.

물론 결과는 정반대였다.

몬스터 군단은 분쇄되었고, 제법 공들여 키운 광신도들은 안전한 도주를 위한 방패막이로 쓰였으니.

‘이렇게 어이없게 당할 줄이야.’

도플갱어는 입맛이 썼다.

자그마치 수만에 달하는 전력이다. 그 강대함은 둘째치고, 오직 그의 명령에 절대복종하는 사병(私兵)들을 잃었다는 점이 더욱 아쉬웠다.

‘그래도 놈이 선택받은 자라는 것을 확인했으니…… 주인님께서는 흡족해하시겠군.’

도무지 그 뜻과 깊이를 알 수 없는 주인을 떠올린 도플갱어는 고개를 절레절레 내저었다.

지난 수십여 년간 보이지 않는 장막 뒤에서 은밀히 세상을 주물러 온 도플갱어였지만, 그조차도 자신의 주인 앞에서는 하찮은 종복에 불과했다.

지금 이 순간에도, 그를 따르고 있는 눈앞의 멍청한 인간들처럼.

“아직 멀었는가.”

짐짓 근엄한 어조로 건넨 한 마디에, 검은 터번으로 전신을 꽁꽁 싸맨 흑의인이 대답했다.

“곧 도착합니다. 위대한 선지자시여.”

“느려 터졌군. 이대로는 따라잡힐 수도 있다. 속력을 더욱 높여라.”

“따라잡힌다 하셨습니까?”

“그래, 놈은 생각했던 것 이상의 괴물이다. 무슨 짓을 벌일지 몰라.”

평소와는 달리 조급함과 두려움마저 뒤섞인 도플갱어의 말에, 호위하듯 도플갱어를 에워싼 채 달려가던 수십여 명의 흑의인들이 시선을 교환했다.

이미 한 시간 가까이 전속력으로 달려온 그들이었다. 한데 여기서 더욱 속력을 높이라니.

힘을 아끼기 위해 제 등에 업혀 있는 도플갱어의 눈치를 보던 흑의인이 결국 조심스럽게 입을 열었다.

“말씀드리기 송구하오나…… 이 이상으로 속도를 높이는 것은 어렵습니다.”

“뭐라?”

“부족한 저희를 용서하시옵소서, 선지자시여.”

말을 하면서도 쉴 새 없이 나아가는 발걸음.

자신을 등에 업은 광신도의 뒤통수를 물끄러미 바라보던 도플갱어가 문득 입을 열었다.

“그래, 그렇구나. 내 잘못이야. 그렇지 않아도 무리하고 있는 그대들의 사정을 모르고 재촉했어.”

“그런 말씀은 감당키 어렵습니다. 거둬 주시옵소서.”

“아니다. 내 어찌 그대들의 마음을 모르겠는가. 함께 자라 온 형제, 자매들을 두고 전장을 떠나면서도 마음이 편치 않았을 테지.”

“그건…….”

“어째서 사악한 이교도들을 피해 이리 쫓기듯이 도망쳐야 하는지도 내심 받아들이기 어려웠을 게야. 그렇지 않나?”

터번 사이로 드러난 흑의인들의 시선이 흔들렸다.

도플갱어의 한 마디, 한 마디가 그들의 마음을 훤히 들여다보듯 정곡을 찌르고 있었다.

수장인 아미르에 의해 오직 선지자를 위한 친위대로 길러진 그들이다.

그러나 모두가 그토록 염원했던 약속의 땅은 척박하기 그지없는 협곡이었고, 푸른 생기와 희망 대신 이교도들이 기다리고 있었다.

그리고 곧이어 벌어진 격렬한 전투와 피를 흩뿌리며 쓰러지는 형제자매들.

하지만 그들은 아랑곳하지 않았다. 신의 뜻을 바로 세우기 위한 성전(聖戰)이라 생각했으니까.

형제자매들의 죽음 역시 거룩한 순교(殉敎)라고 믿었으니까.

적어도 그들이 존경해 마지않는 선지자가, 보잘것없는 몰골로 나타나 전장을 이탈하기 전까지는 그랬다.

‘정말 이것이 옳은 선택인가?’

선지자를 호위하며 끝없이 펼쳐진 서쪽 땅을 향해 사막과 황야를 가로지르고, 오아시스를 지나쳤다.

한순간도 쉼 없이 달려가는 사이, 문득 뇌리를 스친 의문은 점점 커졌다.

신은 전지전능하다. 선지자는 위대한 예언자다.

한데 왜 자신들은 도망치고 있는가. 왜 고작 십분지 일도 되지 않는 이교도의 군세를 피하여 비겁하게 전장을 떠나는가.

아무리 평생토록 다져 온 굳건한 신앙심으로 억눌러 봐도, 마음속에서는 미처 덮지 못한 의문들이 울컥거리며 삐져나온다.

그리고 결국 지금 이 순간, 소리가 되어 혀끝으로 흘러나온다.

“실은, 잘 이해가 되지 않습니다.”

등에 업힌 선지자는 대답하지 않았다.

그 침묵을 허락으로 받아들인 흑의인은 조심스럽게 말을 이었다. 마침내 저 멀리 모습을 드러낸 목적지를 눈에 담으며.

“맞서 싸운다면 승리할 수 있습니다. 선지자께서 항상 저희에게 말씀하시지 않으셨습니까. 신께서는 언제나 우리와 함께하신다고. 그렇기에 늘 승리와 영광만이 가득할 것이라고.”

쐐애애액.

가파르게 쏘아지는 신형들을 따라 휘몰아치는 바람. 그 사이로 다른 흑의인들의 목소리가 섞여들었다.

“저희는 형제자매들을 버리고 도망쳤습니다.”

“신께 버림받을까 두렵습니다.”

“선지자시여. 전능하신 그분께서 무슨 말씀을 전하셨는지, 감히 여쭈어 봐도 되겠나이까.”

바로 그때였다.

묵묵히 그들의 이야기를 듣고만 있던 선지자, 아니 도플갱어가 입을 연 것은.

“멈추어라.”

단 한시도 쉬지 않고 앞으로 나아가던 흑의인들이 걸음을 멈추었다.

등에 업혀 이동하는 동안 소모되었던 힘을 회복한 도플갱어가 땅에 발을 디디며 중얼거렸다.

“드디어 도착했군.”

주위는 쓸쓸하고 황량했다.

한때 세계에서 두 번째로 컸다는 유전(油田)의 흔적은 어디에서도 찾아볼 수 없었고, 풀 한 포기 나지 않은 땅에는 누구의 것인지 모를 백골이 굴러다녔다.

죽음의 땅.

그 광경을 본 순간 흑의인들의 뇌리를 스친 말이었다. 그중 하나가 용기를 내어 물었다.

“이곳이 어디입니까?”

흑의인들도 궁금하긴 매한가지였다. 한낱 종복에 불과한 그들은 그저 명령에 따라 움직였을 뿐, 위대한 선지자의 뜻을 감히 짐작하기 어려웠다.

그리고 다음 순간 귓가에 닿은 한 마디에, 모두의 눈이 부릅떠졌다.

“대격변이라 칭하는 환란의 시절. 잠시나마 그분께서 머무르셨던 땅이다.”

“……!”

“……!”

“나의 주인. 또한 만물의 주인이신 그분께서 말씀하셨다. 인간들에게 가라. 그곳에서 때를 기다려라.”

순간, 공기가 멈춘 듯했다.

넋 나간 눈빛으로 주위를 바라보던 흑의인들이 동시에 무릎을 꿇고 목청껏 부르짖었다.

“오오, 오오오……!”

“인샬라!”

“신은 위대하시다!”

그것은 당연한 반응이었다.

선지자가 모시는 주인은 단 한 분이며, 그분께서 임하셨던 이 땅이야말로 성지(聖地)라 부르기에 부족함이 없었으니까.

그리고 납작 엎드린 채 신의 은총을 부르짖는 그들의 머리 위로, 한 줄기 음성이 이어졌다.

“신께 버림받을까 두렵다 하였느냐.”

어조는 부드러웠다. 보채는 아이를 달래듯.

“그분께서 무슨 말씀을 전하셨는지 듣고 싶다 하였더냐.”

마침내 성지에 이르러 엎드려 절하는 신도들의 머리카락을 쓸어내리는 손길은 따뜻했다. 고통에 신음하는 환자의 아픈 상처를 보듬듯.

“그렇다면 알려 주마.”

하지만 그들을 굽어보는 시선은 부드럽지도, 따뜻하지도 않았다.

그것은 마치 사막의 햇빛이 북풍설한(北風雪寒)으로 변하는 것과 같은 변화였고, 뒤이어 들려온 목소리는 싸늘하게 얼어붙어 있었다.

“네놈들이 얼마나 하잘것없는 것들인지.”

그 순간.

퍼엉! 투두둑.

감격에 차 있던 흑의인들은 눈을 깜빡였다.

땅 깊숙이 묻고 있던 고개를 들자, 사방에 흩뿌려진 붉은 핏물과 살점들이 시야에 들어왔다.

“어……?”

누군가의 입술 사이로 흘러나온 넋 나간 목소리.

그것은 순수한 의문이었고, 받아들일 수 없는 현실이었다.

그리고 그 의문에 대한 답을 찾기도 전에, 흑의인들의 머리 위로 짙은 어둠이 드리워졌다.

쏴아아아악.

등골이 오싹했다. 의지를 벗어난 손발이 석상처럼 굳었다.

일평생 단련한 신체와 마나도, 허리춤에 찬 검도 지금만큼은 무용지물이었다.

아.

외마디 신음.

흑의인들은 난생처음 느끼는 거대한 공포와 충격에 휩싸인 채, 눈앞으로 닥쳐 오는 어둠을 바라보았다.

마치 거울 표면처럼 매끈한 어둠에는, 그들의 얼굴이 고스란히 내비치고 있었다.

‘이건…….’

더는 새어 나오지 않는 목소리. 굳어 버린 전신.

흑의인들은 비명조차 내지르지 못한 채 눈동자를 움직였다. 그들을 감싸 안는 어둠 위로 한 사람의 얼굴이 보였다.

모두를 약속의 땅으로 이끌 위대한 선지자.

아니, 선지자라고 믿었던 ‘그것’이 그들을 바라보며 웃고 있었다.

죽음도 무엇도 아닌, 끔찍한 심연 속 무저갱으로 인도하고 있었다.

“들어라, 이 어리석은 것들아. 나약하고 하찮은 인간들아.”

슈우우욱.

어둠이 싱그러운 생기(生氣)를 빨아들인다. 희끄무레한 수십의 영혼이 홀린 듯이 어둠 속 자신을 향해 흘러 들어갔다.

“이 세상에는 오직 한 분의 왕만이 계실 뿐.”

일곱 개의 구멍을 통해 흘러나온 핏물을, 어둠이 집어삼킨다. 팽팽하던 피부가 쪼그라들고 뼈가 바스라진다.

가까워진 죽음. 혹은 심연.

무저갱으로 곤두박질치는 시야 속에서, 그들은 악마의 마지막 음성을 들었다.

- 신은…….

이미 너희를 버렸다.

아스라이 울려 퍼지는 한 마디.

그것이 마지막이었다.

어둠이 드리워졌던 그곳에 남아 있는 것은 경배하듯 무릎 꿇고 있던 스무 구의 미라.

그리고 지난 수백 년간 그래 왔듯이 새로운 생명을 취한 어느 존재뿐이었다.

아니, 그럴 것이라 생각했다.

화아아악.

폐허 위의 허공에서 눈부신 빛줄기가 터져 나오기 전까지는.

그 아득한 섬광 속에서, 청백색의 불꽃이 넘실거리며 쏟아지기 전까지는.

콰아아아아!

강대한 화염이, 도플갱어의 눈동자를 푸르게 물들였다.
```

## Final English reading copy

```markdown
# Chapter 824

When dawn comes, the darkness retreats.

It was one of those truths as obvious as water flowing downhill. But for those fleeing someone’s pursuit, it wasn’t exactly welcome news.

Especially when the pursuer was such a monster that it was hard to believe he was even human.

*Already?*

The Doppelganger bit its lip as it watched the sky slowly brighten.

It was too soon. No—in truth, it had wasted more time than expected.

*Everything should have been over before daybreak at the latest.*

The Doppelganger knew that no amount of regret or brooding would change reality.

Its carefully laid plans had gone off course long ago. And at the center of it all, at the very beginning, was that bastard.

*Jin Taekyung.*

Throb.

Just thinking of his name sent stabbing pains through the Doppelganger’s body.

Having died at Jin Taekyung’s hands hundreds of times, the Doppelganger shuddered as it remembered his terrifying might.

*I should never have approached him in the first place.*

It had been a mistake. Greed.

After absorbing Yamamoto Genji, it should have left in a hurry—or never revealed itself at all.

*I only needed to take a little more. Just a little.*

Its original targets had been other humans.

The many Hunters left behind in the rear. If it could absorb their mana and life force, it would have achieved its goal.

*Damn it.*

But Jin Taekyung hadn’t let the Doppelganger go easily.

He’d handled it like a slave, never allowing it to leave his sight.

That had been a misfortune for the Doppelganger—and good fortune for every Hunter besides Jin Taekyung.

If the Doppelganger had escaped his grasp, put on Yamamoto Genji’s skin, and headed for the main force in the rear… it would have led countless monsters and fanatics to turn the desert red with blood.

Of course, the outcome had been the opposite.

The monster army was crushed, and the fanatics it had spent considerable effort raising were used as a shield to ensure its escape.

*I can’t believe I got beaten this badly.*

The Doppelganger’s mouth turned bitter.

It had lost a force tens of thousands strong. More than their strength, it regretted losing its private army, soldiers who obeyed its every command without question.

*Still, I confirmed he’s the Chosen One… Master will be pleased.*

Thinking of its master, whose intentions and depths it could never fathom, the Doppelganger shook its head.

For decades, it had secretly manipulated the world from behind an unseen curtain. Yet even it was nothing but a lowly servant before its master.

Just like the foolish humans following it now.

“Are we still far?”

The Doppelganger asked in a deliberately grave voice. The man in black, wrapped from head to toe in a black turban, answered.

“We will arrive shortly, O great Prophet.”

“You’re unbearably slow. At this rate, we could be caught. Pick up the pace.”

“You say we could be caught?”

“Yes. He’s a greater monster than I expected. I don’t know what he might do.”

At the Doppelganger’s words, laced with an unusual mixture of impatience and fear, the dozens of men in black running around it like an escort exchanged glances.

They’d been running at full speed for nearly an hour. And now it wanted them to go even faster?

The man in black carrying the Doppelganger on his back to conserve its strength glanced at it, then finally spoke with care.

“I’m sorry to say this, but… we cannot go any faster.”

“What?”

“Forgive us for our shortcomings, O Prophet.”

Even as he spoke, his feet never stopped moving.

The Doppelganger stared at the back of the fanatic carrying it, then suddenly spoke.

“I see. This is my fault. I pressed you without considering that you were already pushing yourselves.”

“We are unworthy of such words. Please, take them back.”

“No. How could I not understand your hearts? You must have been troubled to leave behind the brothers and sisters you grew up with and abandon the battlefield.”

“That’s…”

“You must have struggled to accept why we had to flee like this, chased away by evil heretics. Isn’t that so?”

The eyes of the men in black wavered beneath their turbans.

Every word from the Doppelganger struck home, as if it could see straight into their hearts.

They had been raised by their leader, Amir, to serve as a personal guard for the Prophet alone.

But the Promised Land they had all longed for was nothing but a barren canyon, and instead of green life and hope, heretics awaited them.

Then came the fierce battle, and their brothers and sisters fell, their blood spraying across the ground.

But they hadn’t cared. They had believed it was a holy war to uphold God’s will.

They had believed their brothers’ and sisters’ deaths were holy martyrdom.

At least, they had—until the Prophet they so revered appeared in a wretched state and left the battlefield.

*Was this really the right choice?*

Escorting the Prophet, they crossed desert and wilderness toward the endless western lands, passing oases along the way.

As they ran without a moment’s rest, a question that had once flickered through their minds began to grow.

God was omniscient and omnipotent. The Prophet was a great oracle.

Then why were they running? Why were they cowardly abandoning the battlefield to flee an enemy force less than a tenth their size?

No matter how hard they tried to suppress them with the unwavering faith they had built over a lifetime, questions they couldn’t quite bury kept welling up from inside.

And at last, in that very moment, the questions spilled from their lips.

“To be honest, I don’t understand.”

The Prophet on his back gave no answer.

Taking the silence as permission, the man in black cautiously continued, eyes fixed on their destination, now visible in the distance.

“If we fought back, we could win. Didn’t you always tell us that God was with us? That we would always be blessed with victory and glory?”

*Whoooosh.*

Wind roared around the figures hurtling forward. Other voices from the men in black joined in.

“We abandoned our brothers and sisters and ran.”

“We’re afraid God will abandon us.”

“Prophet, dare we ask what the Almighty told you?”

That was when the Prophet—no, the Doppelganger, which had been listening in silence—spoke.

“Stop.”

The men in black, who hadn’t paused for even a moment, came to a halt.

Having recovered some strength while being carried on their backs, the Doppelganger set its feet on the ground and muttered:

“We’ve finally arrived.”

The area was desolate and barren.

There was no sign of what had once been said to be the world’s second-largest oil field. On the land where not a blade of grass grew, bleached bones of unknown origin lay scattered.

A land of death.

That was what came to the men in black as they took in the sight. One of them found the courage to ask:

“Where are we?”

The others were just as curious. They were mere servants, following orders; they could hardly presume to guess the will of the great Prophet.

Then, at the next words they heard, everyone’s eyes flew wide open.

“During the time of tribulation known as the Great Cataclysm, this was the land where He stayed, if only for a while.”

“……!”

“……!”

“My master. The master of all creation. He told me: Go to the humans. Wait there for the time to come.”

For a moment, it was as if the air had stopped.

Staring around in a daze, the men in black dropped to their knees as one and cried out at the top of their lungs.

“Ooh, oooooh…!”

“Inshallah!”

“God is great!”

Their reaction was only natural.

The Prophet served only one person, and this was the land where that person had once descended. It was worthy of being called the Sacred Land.

Then, above their heads as they lay flat and cried out for God’s blessing, came a voice.

“You said you were afraid God would abandon you.”

Its tone was gentle, like someone soothing a fussy child.

“You said you wanted to hear what He had told me.”

A hand brushed over the hair of the worshipers prostrating themselves upon finally reaching the Sacred Land. It was warm, like a hand tending the painful wound of a patient groaning in agony.

“Then I’ll tell you.”

But the gaze looking down on them was neither gentle nor warm.

It was a change like the desert sun turning into a bitter northern blizzard. The voice that followed was cold as ice.

“Just how worthless you are.”

At that moment—

*Boom! Thud-thud.*

The men in black, overcome with emotion, blinked.

When they raised their heads from the ground, red blood and pieces of flesh were scattered all around them.

“Huh…?”

A dazed voice slipped from someone’s lips.

It was a pure question—and a reality they couldn’t accept.

Before they could find an answer, a deep darkness fell over the men in black.

*Whoooosh.*

A chill ran down their spines. Their hands and feet, beyond their control, stiffened like stone.

Their bodies, honed through a lifetime of training, their mana, and the swords at their waists were all useless now.

Ah.

A single groan.

Overcome by a vast terror and shock they had never felt before, the men in black stared at the darkness bearing down on them.

The darkness was as smooth as a mirror, and their faces were reflected in it, clear as day.

*This is…*

Their voices wouldn’t come out. Their bodies had gone rigid.

Unable even to scream, the men in black moved their eyes. Above the darkness enveloping them, they saw a face.

The great Prophet who would lead them all to the Promised Land.

No—the thing they had believed was the Prophet was looking down at them, smiling.

It was leading them not to death, or anything else, but into a bottomless pit within a dreadful abyss.

“Listen, you fools. You weak, worthless humans.”

*Fwoooosh.*

The darkness drained the fresh vitality from their bodies. Dozens of pale souls flowed as if entranced toward the Doppelganger within the darkness.

“There is only one king in this world.”

The darkness swallowed the blood flowing from the seven openings in their faces. Their taut skin shriveled, and their bones crumbled.

Death drawing near. Or perhaps the abyss.

As their vision plunged headlong into the bottomless pit, they heard the devil’s final words.

—God…

Had already abandoned you.

The words echoed faintly.

That was the end.

Where the darkness had fallen, twenty mummified corpses remained, kneeling as though in worship.

And only one being remained, having taken new life as it had for the past several hundred years.

Or so it thought.

*Fwoooosh.*

That was, until a dazzling beam of light erupted in the air above the ruins.

Until blue-white flames surged and poured forth from within that distant radiance.

*Kwaaaaaang!*

Powerful flames washed the Doppelganger’s eyes blue.
```
