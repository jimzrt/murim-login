<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0823.txt",
      "sha256": "e6c7a29b7b01e3c61632bb609d88f7ecd1b0b10ae2bddebcff12881970914b4c",
      "bytes": 13492
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4bb8ed07a2c81d442b33c3554fdc261f366f0767b439b6eb5a3681c330eaa266",
      "bytes": 1978
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3aa845c898a4d7baa3b82163a8c21152b9cc8866113c3b3793c09c7a03e2878f",
      "bytes": 226544
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "4b914ed0dac9f5e26888257e381576d2061e646bbf83644dbb8906fc4d28676a",
      "bytes": 831
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "6236a4a5dd0b88255ebde616a126c33ac366216137a7c6352d7ae0b4703d5262",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e92a4395cb7c225d093bc865c3829871b4a9e2331d49ebbf748608ded2e8140e",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "34a3ad11deecf4a9d9c16dd823c0a636f97b1fe6c4ac4ae34f4dfad98672abb9",
      "bytes": 622
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "5c09df37edf440a1f1ed2d771249b44d35ab3380802c37acc6d90e33035cac61",
      "bytes": 724
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "cb1d5d0a3787501af4a81fb1b32001a17ac60354ef4115186da431e0e218f176",
      "bytes": 250268
    }
  ],
  "estimated_tokens": 10295
}
-->

# Durable State Update — Chapter 823

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
1 and safe_through 823. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 823. Profile updates may replace only one
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
  "chapter": 823,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 823,
    "continuity_sources": [823],
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
    "The Doppelganger’s absorbed lives are dwindling; its left arm was torn off, and its regeneration is slow after forcing Blink beyond its normal range.",
    "The Doppelganger is fleeing west with a small escort; Jin intends to stop its plan, which it has spent more than thirty years building.",
    "The battle in the Rub’ al Khali Desert ended at dawn; Jin killed Hamid Shah Masoud after defeating the attackers who charged him.",
    "Jin can control weapons within a radius of dozens of meters using force from his Middle Dantian, directing them around allies and toward selected targets.",
    "The Skeleton King is Jin’s friend and ally; he distinguishes selfless human sacrifice from the fanatics’ deaths in service of a deception."
  ],
  "continuity_sources": [
    821,
    822
  ],
  "open_questions": [
    "Who is the Doppelganger’s master, what is the plan, and why must the target be avoided until it is complete?",
    "What does the Chosen One designation mean?",
    "Will Jin reach the Doppelganger before it escapes?",
    "Is Magic Johnson human?"
  ],
  "safe_through": 822,
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
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 도사      | **Daoist**                                                      |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 심력 | **mental strength** | Inner mental capacity injured by Jongni Chu's feint. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 쓰촨 | **Sichuan** | Variant spelling used for the region associated with the pattern Jin recognizes. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 마수드 | **Masoud** | Rebel named during the battlefield footage. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 하미드 | **Hamid** | Amir’s subordinate, addressed by name. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 진태경 | 선지자 | enemy commander addressed by Jin | The Prophet | blunt and informal | Jin asks where The Prophet is while confronting the Manticore Lord. |
| 존슨 | 진태경 | allied friend and comrade-in-arms | Jin | familiar and conversational | Johnson calls Jin 진 while asking what he was thinking. |
| 진태경 | 도플갱어 | enemy | you; the Doppelganger | blunt and informal | Jin directly challenges the Doppelganger and demands to know what it wants. |

## Listed compact profiles

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 821
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger is a powerful being from the Demon Realm that spent decades manipulating events in the human world.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** Not established
- **Relationships:** It served an unnamed master who sent it to this world and ordered it to avoid the target until the master’s plan was complete; it regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 822
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 822
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 822
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 822
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” who concealed itself for decades as Muninn.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors and is revered by its followers; it made a pact with Michael Silbert during the 2020 Battle of Paris, where Michael killed the surviving humans in exchange for being spared.

## Korean source

```text
＃823화



철컹. 투두둑.

무수한 병장기가 피로 물든 지면 위로 떨어져 내린다. 수천의 광신도들이 물결처럼 무릎을 꿇는다.

동쪽으로부터 시작된 어스름한 새벽빛이 그 광경을 비추었다.

마침내 승리가 찾아온 전장을.

그리고 이 믿을 수 없는 승리를 가져온 한 청년을.

‘진태경.’

무릎 꿇은 패자들은 그 이름 앞에서 감히 고개조차 들지 못했고, 승자들은 경이에 가득 찬 눈동자로 자신들의 젊은 맹주를 바라보았다.

열 배가 넘는 수적 열세.

죽음조차 두려워하지 않고 달려들던 미친 광신도들.

헌터들은 내심 두려웠다.

두 번 다시 가족들을 만나지 못할까 봐. 이 이름 모를 협곡에서 자신들이 쓰러진다면, 더욱 큰 재앙이 산 자들을 집어삼킬까 봐.

하지만 그들이 잠시나마 품었던 두려움이 무색하게도, 진태경은 한순간에 이 거대한 전투를 마무리 지었다.

압도적이었고, 한편으로는 신성(神性)했다.

살아남은 이들 모두가 알고 있었다.

진태경이 베어 낸 것은 적들의 살과 뼈만이 아니다. 그는 광신도들의 마음을 꺾었다. 그들 스스로 무기를 내려놓게 만들었다.

마치 신화 속 한 장면처럼.

‘기적이 있다면…… 바로 이런 것이겠지.’

매직 존슨은 문득 가슴속이 울렁이는 것을 느꼈다. 하염없이 진태경을 바라보는 대마도사의 시선은 잔물결처럼 떨리고 있었다.

‘그를 닮았다. 놀라울 만큼.’

아지랑이처럼 피어오른 옛 기억이 망막 위로 드리운다.

삼십여 년 전의 케케묵은 기억. 그러나 ‘그’와 함께한 모든 순간은 지금까지도 생생하다.

매직 존슨이 두 눈으로 똑똑히 지켜보았던 기적은, 그 위대한 업적은 인류가 존재하는 한 영원히 기억될 것이다.

지금 이 순간, 고요해진 전장의 중심에서 홀로 우뚝 서 있는 어느 젊은 영웅도 함께.

그러나 동시에 매직 존슨은 알고 있었다.

이 세상에 존재하는 무언가를 얻기 위해서는, 심지어는 기적조차도 합당한 값을 치러야 한다는 것을.

‘등가교환(等價交換)이야말로 불변의 법칙.’

진태경을 응시하던 매직 존슨의 눈빛이 깊숙이 가라앉은 그때. 그가 천천히 들어 올린 스태프의 끝에서 눈부신 빛이 흘러나왔다.

화아아악.

치열했던 대전투의 끝을 알리는 섬광이 어둠을 몰아내고 새벽을 밝힌다.

따스한 온기를 머금은 그 빛에 맞닿은 헌터들은 그제야 도저히 믿어지지 않던 현실을 깨달았다.

그들이 승리했다.

바로 오늘, 새로운 역사의 한 줄을 새로 썼다.

차차차창!

피와 살점으로 범벅된 날붙이가 하늘을 찌르고.

와아아아아아!

거대한 함성이 협곡을 뒤흔들었다.

그것은 승리로 인한 기쁨이요, 죽은 동료에 대한 애도인 동시에 오롯이 한 사람에게 바치는 경외.

하지만 그들 중 대다수는 알지도, 보지도 못했다.

사방에서 쏟아지는 환호를 받으며 우뚝 선 젊은 영웅의 눈꼬리가 파르르 떨리는 모습을.

자꾸만 손아귀에서 미끄러지는 창대를 있는 힘껏 말아 쥔 손가락이 새하얗게 물들어 있는 광경을.

‘……빌어먹을.’

욕설을 삼킨 진태경은 가슴 깊숙한 곳에서 울컥 솟구치는 뜨거운 기운을 억눌렀다.

자꾸만 흐릿해져 가는 시야, 이명(耳鳴)이 맴도는 귓가에는 헌터들의 환호와 시스템 알림이 혼잡하게 뒤섞여 파고들었다.



- [Lv.140 하미드 샤 마수드]를 처치하셨습니다!

- 상당량의 경험치와 명성을 획득하셨습니다!

- 레벨 업!

- 레벨 업의 효과로 모든 상태 이상이 해제됩니다!

- 레벨 업의 효과로 일부 상처가 치유됩니다!

- 특수 디버프, [부서진 신체]가 치유의 힘을 거부합니다!

- 상태 이상, [심력 고갈]이 치유의 힘을 거부합니다!

- [중단전]이 한계에 다다랐습니다! 한시라도 빨리 휴식을 취하여 심력을 회복하십시오!



현재 진태경이 처한 상황은 시스템이 알려 준 그대로였다.

신체의 상처와 피로는 회복되었으나, 중단전(中丹田)은 시스템으로도 치유할 수 없는 영역. 앞서 그가 보인 재앙과도 같은 파괴력은 결코 헐값으로 얻어 낼 수 있는 수준의 것이 아니었다.

욱신.

이미 한계까지, 아니 한계 이상으로 힘을 쥐어짜 낸 탓에 서 있는 것만으로도 힘이 벅찼다.

심장 어림에서 전해져 오는 고통과 정신적인 피로는 끊임없이 몸을 좀먹으며 속삭였다.

전투는 끝났다고.

네 역할은 끝났으니, 지금부터라도 휴식을 취하라고.

“그래, 할 만큼 하긴 했지.”

공허한 뇌까림이 혀끝에서 흩어진다.

진태경은 흐릿한 시야 너머로 환호하는 헌터들을 바라보았다.

함께 몇 번의 전투를 겪으며 익숙해진 면면들.

군데군데 빈 자리가 눈에 띄긴 했지만, 이번 전투로 목숨을 잃은 헌터들의 숫자가 많지 않다는 것쯤은 알아볼 수 있었다.

만약 중단전의 효용을 한계 이상으로 발휘하지 않았다면, 아마 살아남은 헌터 중 절반 이상은 지금쯤 전장에 널브러진 채 차갑게 식어 가고 있었을 터.

진태경의 생각은 결코 과장된 것이 아니었다.

그는 힘들었던 격전을 단숨에 승리로 이끌었고, 더 많은 피가 흐르는 것을 막았다.

역사에 길이 남을 대전투를 그 홀로 마무리 지었다.

하지만…….

‘아직 끝나지 않았다.’

진태경은 창대를 말아 쥔 손아귀에 힘을 더했다. 자꾸만 감기려는 눈을 억지로 부릅뜨고, 저 멀리 사막과 황야가 펼쳐진 서쪽을 바라보았다.

‘해야 할 일이 남았어.’

정광(正光)이 꺼지지 않은 청년의 눈이 끝없이 늘어선 지평선을 응시한다.

그의 시선은 이미 시야에서 사라져 버린 누군가를 좇고 있었다.

‘도플갱어.’

새벽이 찾아오는 지금 이 순간에도, 도플갱어가 모습을 감춘 서쪽 땅은 어둠에 잠겨 있었다.

마치 놈의 그림자가 드리워진 것처럼. 그리고 뒤이어 찾아올 거대한 전쟁을 예고하는 것처럼.

‘가야 한다.’

순간 진태경의 머릿속에 떠오른 생각은, 의지를 넘어 사명에 가까웠다.

그는 나아가야 했다. 여기서 멈춰서는 안 됐다.

서쪽 저 멀리 사라진 도플갱어를 쫓아, 머지않은 미래에 들이닥칠 재앙을 막아야 했다.

저벅.

홀린 듯이 앞으로 나아가는 걸음.

그러나 이미 밑바닥을 드러낸 심력(心力)은 몸뚱어리를 움직이지 못했다.

비틀.

앞으로 걸어라.

그 간단한 명령을 제때에 전달받지 못한 다리에 힘이 풀린다. 가슴으로부터 쥐어짜는 듯한 통증이 심신을 방해했다.

‘제기랄.’

고작 두 번째 걸음 만에 맞닥트린 벽.

진태경은 서서히 기울어지는 시야를 느끼며 헛웃음을 삼켰다. 그리고 문득, 눈앞이 어두워졌다고 느꼈을 때.

스륵, 툭.

앞으로 기울어지던 이마가 단단한 무언가에 닿았다.

뒤이어 등 뒤에서 불쑥 뻗어진 손이 힘없이 허물어지려던 신형을 일으켜 세우고, 이명이 울려 퍼지는 귓가로 두 줄기의 목소리가 파고들었다.

“고생했어, 진.”

“정신차려라. 인간.”

진태경은 눈을 깜빡였다.

쓰러지려는 자신을 일으켜 세운 손의 주인도, 앞을 가로막은 단단한 벽의 정체도 이제야 알 것 같았다.

‘매직 존슨. 그리고 스켈레톤 킹.’

그들이 왔다.

한 인간과 몬스터. 아니, 친구들이 왔다.

자신을 돕기 위해.

까득.

아득한 통증과 함께 흐려졌던 시야가 다시금 또렷해진다.

혀에서 흘러나온 핏물을 삼킨 진태경은 고개를 들었다. 더없이 반가운 얼굴들이 그를 기다리고 있었다.

“하.”

순간 입가를 비집고 흘러나온 웃음에, 스켈레톤 킹이 굳은 얼굴로 매직 존슨을 향해 물었다.

“못생긴 놈이 왜 재수 없게 실실 쪼개지? 결국 미친 건가?”

“자네야말로 재수 없는 소리 작작하고 입 다물어. 이봐, 진. 내 말 들려?”

“인간아. 지금 내 손가락이 몇 개냐.”

진태경이 힘없는 목소리로 대답했다.

“목소리 잘 들려요. 손가락도 보이고.”

“개수를 말해라. 이 못생기고 아둔한 놈아.”

“한 개. 그런데 그 손가락 부러지고 싶지 않으면 적당히 하고 내려라.”

눈앞에서 중지를 흔들어 대던 스켈레톤 킹이 고개를 끄덕였다.

“다행히 정상이군.”

그 모습에 실소를 흘리던 진태경이 기침을 토해 냈다.

“최 팀…… 쿨럭, 최 팀장님은?”

“잘 있다. 조금 다치긴 했지만.”

“그래? 확실하지?”

“믿어라. 거짓말이 아니니까.”

안도의 한숨을 내쉰 진태경은 힘주어 허리를 곧게 폈다.

여전히 숨은 가쁘고 감각은 무디다. 그러나 이곳에서 멈출 수는 없었다.

“존슨.”

때로는 작은 행동, 한마디 말에 모든 것이 담겨 있는 법.

진태경의 짧은 부름에, 무언가를 직감한 매직 존슨이 대답했다.

“안 돼.”

“가야 합니다. 아시잖아요.”

“알지.”

매직 존슨이 굳은 얼굴로 덧붙였다.

“지금 네가 쉬어야 한다는 것도.”

대마도사의 눈에는 똑똑히 보였다. 억지로 정신을 붙잡고 있을 뿐, 이미 한계에 다다라 있는 진태경의 상태가.

하지만 무모함은 젊은이들의 전유물이었다.

눈앞의 청년이 언제나 늘 그러했듯이.

“텔레포트 마법을 써 주세요.”

“제기랄, 진. 미쳤어?”

“이건 부탁이 아닙니다.”

“그렇다면 지금 이 시간부로, 난 세계 헌터 연맹에서 나가도록 하지.”

“그럼 그렇게 하세요.”

진태경이 머리 하나는 더 큰 매직 존슨을 올려다보며 말을 이었다.

“하지만 제가 사표를 수리하기 전까지는, 제 명령을 들어야 할 겁니다.”

“……!”

“어서요. 존슨.”

매직 존슨은 말문이 턱 막히는 것을 느꼈다.

사표니 뭐니 하는 이야기는 결국 조잡한 말장난에 불과하다.

그러나 진태경의 두 눈동자에 깃든 저 의지는, 당장이라도 꺼질 듯한 의식을 부여잡은 사명감은 단 한 방울의 거짓도 깃들어 있지 않은 진실이었다.

‘빌어먹을.’

그 눈을 똑바로 마주할 자신이 없다. 이런 선택을 할 수 밖에 없는 스스로가 부끄러웠다.

자신도 모르게 두 눈을 질끈 감았다 뜬 매직 존슨이 이를 악물었다.

“……이건 미친 짓이야. 지금처럼 마력 농도가 짙은 상황에서의 텔레포트 마법은 자살 행위나 마찬가지라고.”

진태경이 희미하게 웃으며 입을 열었다.

“그때 생각나네요.”

“뭐?”

“중국 쓰촨. 그곳에서도 같은 말을 했었잖아요. 그리고 보기 좋게 성공했었고.”

“……!”

“절 보내 줘요. 처음 선지자가, 아니 도플갱어가 알려 줬던 그 장소로.”

진태경을 바라보는 매직 존슨의 동공이 파르르 떨렸다.

말려야 하는데, 분명히 말려야 하는데.

빌어먹을 대마도사의 두뇌는 이미 계산과 동시에 합리적인 추론을 내리고 있었다.

‘가능성은 충분하다.’

지금과 같은 마력 농도에서 펼치는 텔레포트 마법은 이미 아크 리치 토벌전 당시 한 차례 시도해 본 적 있다.

현존하는 마법사 중에서도 한 손가락 안에 꼽히는 매직 존슨이었기에, 그리고 그 대상이 진태경이었기에 가능했던 일이었다.

‘텔레포트 마법이 아니라면, 진이 아니라면…… 그 누구도 도플갱어를 막지 못하겠지.’

진태경의 제안은 무모했지만, 외면할 수 없는 현실이기도 했다.

이미 도플갱어가 전장을 이탈하여 도주한 지 상당한 시간이 흐른 지금, 놈을 따라잡는 것은 불가능에 가까웠다.

단, 텔레포트 마법을 사용한다면.

또한 이토록 위험한 텔레포트 마법을 견뎌 낼 수 있는 이가 있다면, 이야기는 달라진다.

참으로 잔인하게도.

“Fuck.”

매직 존슨은 힘없이 욕설을 중얼거렸다. 어느새 누구의 도움도 없이 홀로 선 진태경이 그를 똑바로 응시하고 있었다.

그리고 그런 진태경의 옆에는, 이 위험한 동행에 함께하기를 자처한 누군가가 있었다.

“이 몸도 함께 간다. 넌 이곳을 지켜라.”

스켈레톤 킹. 죽음마저 극복한 언데드의 군주.

그를 본 순간, 매직 존슨은 자신에게 더 이상 물러설 곳이 남아있지 않다는 것을 깨달았다.

“한 가지만 약속해.”

우우웅.

마나를 머금은 스태프가 몸을 떨었다. 휘황한 섬광 너머, 그의 목소리가 희미하게 울려 퍼졌다.

“살아 돌아와, 반드시.”

화아아악.

아득한 섬광이, 공간을 집어삼켰다.
```

## Final English reading copy

```markdown
# Chapter 823

*Clang. Clatter.*

Countless weapons fell onto the blood-soaked ground. Thousands of fanatics sank to their knees like a wave.

The faint light of dawn, rising in the east, shone on the scene.

The battlefield where victory had finally arrived.

And the young man who had brought about this unbelievable victory.

*Jin Taekyung.*

The defeated, kneeling before that name, did not dare raise their heads. The victors gazed at their young Alliance Leader with eyes full of wonder.

Outnumbered by more than ten to one.

Mad fanatics who charged without fear of death.

The Hunters had been afraid.

Afraid they would never see their families again. Afraid that if they fell in this nameless canyon, an even greater calamity would swallow up those who remained alive.

But their brief fear had been rendered meaningless. Jin Taekyung had ended this massive battle in an instant.

He had been overwhelming—and, in a way, divine.

Everyone who survived knew it.

Jin Taekyung hadn’t just cut through the enemy’s flesh and bone. He had broken the fanatics’ spirits. He had made them lay down their weapons of their own accord.

Like a scene from a myth.

*If miracles exist… this must be what one looks like.*

Magic Johnson suddenly felt something stir in his chest. The Grand Mage’s gaze, fixed on Jin Taekyung, trembled like ripples on a pond.

*He reminds me of him. Astonishingly so.*

Old memories rose like heat haze, drifting across his eyes.

Memories more than thirty years old, worn with time. Yet every moment he had spent with *him* remained vivid.

The miracle Magic Johnson had witnessed with his own eyes—*his* great achievement—would be remembered forever, as long as humanity endured.

And so would the young hero standing alone at the center of the now-quiet battlefield, in this very moment.

But Magic Johnson also knew.

To gain anything in this world—even a miracle—one had to pay a price.

*Equivalent exchange is the one unchanging law.*

Just then, as Magic Johnson’s gaze settled deeply on Jin Taekyung, dazzling light streamed from the tip of the staff he slowly raised.

*Fwoooosh.*

A flash that heralded the end of the fierce battle drove back the darkness and lit the dawn.

The Hunters touched by that light, carrying a gentle warmth, finally understood the reality they could hardly believe.

They had won.

Today, they had written a new line in history.

*Clang-clang-clang!*

Blades smeared with blood and flesh thrust toward the sky.

“Waaaaaaah!”

A tremendous roar shook the canyon.

It was joy at their victory, mourning for their dead comrades, and reverence offered wholly to one man.

But most of them neither knew nor saw it.

The young hero standing tall amid the cheers pouring in from every direction, his eyes twitching.

His fingers, gripping the spear shaft as tightly as they could because it kept slipping from his grasp, had turned white.

*…Fuck.*

Jin Taekyung swallowed a curse and suppressed the hot surge rising from deep in his chest.

His vision kept blurring. In his ringing ears, the Hunters’ cheers and the System notifications crowded together in a jumble.

> **System**
> - You have defeated Lv. 140 Hamid Shah Masoud!
> - You have gained a substantial amount of EXP and Fame!
> - Level Up!
> - All status ailments have been removed as a Level Up effect!
> - Some wounds have been healed as a Level Up effect!
> - Special debuff Broken Body rejects the healing effect!
> - Status ailment Mental Strength Depleted rejects the healing effect!
> - Middle Dantian has reached its limit! Rest as soon as possible to recover your mental strength!

Jin Taekyung’s situation was exactly as the System had described.

His physical wounds and fatigue had recovered, but his Middle Dantian was beyond the System’s power to heal. The catastrophic force he had unleashed earlier was never something he could wield for a cheap price.

*Throb.*

He had already wrung himself out to his limit—and then beyond it. Even standing took more strength than he had.

Pain radiating from around his heart and mental exhaustion gnawed at him without pause, whispering:

The battle is over.

Your part is done. Rest now.

“Yeah. I did enough, didn’t I?”

The empty murmur scattered from his lips.

Through his blurred vision, Jin Taekyung looked at the cheering Hunters.

Faces he had grown familiar with after fighting alongside them several times.

He could see a few gaps here and there, but he could tell that not many Hunters had lost their lives in this battle.

If he hadn’t pushed the Middle Dantian beyond its limits, more than half of the Hunters who had survived would probably be sprawled across the battlefield by now, growing cold.

Jin Taekyung wasn’t exaggerating.

He had turned a grueling battle into a swift victory and stopped more blood from being spilled.

He had single-handedly brought a battle that would go down in history to an end.

But…

*It’s not over yet.*

Jin Taekyung tightened his grip around the spear shaft. He forced his eyes open, though they kept trying to close, and looked toward the west, where desert and wilderness stretched into the distance.

*There’s still something I have to do.*

The light in the young man’s eyes had not gone out as he stared at the endless horizon.

His gaze was already chasing someone who had vanished from sight.

*The Doppelganger.*

Even now, as dawn arrived, the western land where the Doppelganger had disappeared remained shrouded in darkness.

As though its shadow had fallen over it. As though it were a warning of the great war to come.

*I have to go.*

The thought that flashed through Jin Taekyung’s mind was more than a matter of will. It was almost a duty.

He had to move forward. He couldn’t stop here.

He had to pursue the Doppelganger, vanished far to the west, and stop the calamity that would strike in the not-too-distant future.

*Step.*

He moved forward as if entranced.

But his mental strength, already drained to the dregs, wouldn’t let his body move.

He staggered.

*Walk forward.*

His legs failed to receive that simple command in time. A wrenching pain squeezed at his chest, interfering with both body and mind.

*Damn it.*

He’d hit a wall after only his second step.

Feeling his vision slowly tilt, Jin Taekyung stifled a hollow laugh. And just as everything suddenly seemed to go dark—

*Slide. Tap.*

His forehead, pitching forward, touched something solid.

Then a hand reached out from behind him and pulled his collapsing body upright. Two voices slipped into his ringing ears.

“You did good, Jin.”

“Pull yourself together, human.”

Jin Taekyung blinked.

He thought he finally knew who owned the hand holding him up, and what the solid wall in front of him was.

*Magic Johnson. And the Skeleton King.*

They had come.

A human and a monster. No—his friends had come.

To help him.

*Crack.*

The vision that had blurred with that distant pain grew clear again.

Jin Taekyung swallowed the blood on his tongue and raised his head. Familiar faces were waiting for him.

“Ha.”

At the laugh that slipped from his lips, the Skeleton King turned to Magic Johnson, his expression stiff.

“Why’s that ugly bastard grinning like an idiot? Is he finally going crazy?”

“You’re the one who should quit saying idiotic things and shut your mouth. Hey, Jin. Can you hear me?”

“Human. How many fingers am I holding up?”

Jin Taekyung answered weakly.

“I can hear you fine. And I can see your fingers.”

“Tell me how many, you ugly, dim-witted bastard.”

“One. But if you don’t want me to break it, quit waving it around and lower it.”

The Skeleton King had been waggling his middle finger in front of him. He nodded.

“Good. You’re still sane.”

Jin Taekyung gave a quiet snort, then coughed.

“Team Leader Choi… *cough*, how is he?”

“He’s fine. A little injured, but he’s all right.”

“Really? You’re sure?”

“Trust me. I’m not lying.”

Jin Taekyung let out a relieved sigh and straightened his back with effort.

His breathing was still ragged, and his senses dull. But he couldn’t stop here.

“Johnson.”

Sometimes a small gesture or a single word could say everything.

Magic Johnson sensed what he meant from Jin Taekyung’s brief call and answered.

“No.”

“I have to go. You know that.”

“I do.”

Magic Johnson added, his expression hard:

“I also know you need to rest.”

The Grand Mage could see it clearly. Jin Taekyung was barely holding on to consciousness through sheer force of will, already at his limit.

But recklessness belonged to the young.

As it always had with the young man before him.

“Please use Teleport magic.”

“Damn it, Jin. Are you crazy?”

“This isn’t a request.”

“Then as of this moment, I’m leaving the World Hunter Federation.”

“Then do that.”

Looking up at Magic Johnson, who was a head taller than him, Jin Taekyung continued:

“But until I accept your resignation, you’ll have to follow my orders.”

“……!”

“Come on, Johnson.”

Magic Johnson felt his words catch in his throat.

All this talk about resigning was just a clumsy play on words.

But the will in Jin Taekyung’s eyes, that sense of duty holding him to an awareness that seemed on the verge of going out, was the unvarnished truth.

*Damn it.*

He couldn’t bring himself to look into those eyes. He was ashamed of himself for having no choice but to make it.

Magic Johnson squeezed his eyes shut without meaning to, then opened them and gritted his teeth.

“……This is insane. Using Teleport magic with the magical power concentration this high is practically suicide.”

Jin Taekyung smiled faintly.

“That takes me back.”

“What?”

“Sichuan, China. You said the same thing there. And we pulled it off just fine.”

“……!”

“Send me to the place the Prophet—no, the Doppelganger—first revealed.”

Magic Johnson’s pupils trembled as he looked at Jin Taekyung.

He had to stop him. He absolutely had to stop him.

But the Grand Mage’s mind was already calculating, already reaching a reasonable conclusion.

*There’s a good chance it’ll work.*

They had already tried casting Teleport under magical power concentrations like this once, during the battle to defeat the Arch Lich.

It had been possible because Magic Johnson was one of the best mages alive—and because the person he was transporting was Jin Taekyung.

*If it isn’t Teleport magic, if it isn’t Jin… no one else can stop the Doppelganger.*

Jin Taekyung’s proposal was reckless, but it was also a reality he couldn’t ignore.

A considerable amount of time had already passed since the Doppelganger fled the battlefield. Catching up to it would be almost impossible.

But if they used Teleport magic—

And if there was someone who could endure Teleport magic this dangerous, things would be different.

How cruel.

“Fuck.”

Magic Johnson muttered a curse weakly. Jin Taekyung was standing on his own now, without anyone’s help, looking straight at him.

And at Jin Taekyung’s side stood someone who had volunteered to join him on this dangerous journey.

“I’m going with him. You stay here and protect this place.”

The Skeleton King. Lord of the undead, who had overcome even death.

The moment Magic Johnson saw him, he realized there was nowhere left to retreat.

“Promise me one thing.”

*Whummm.*

The staff, filled with mana, trembled. Beyond the dazzling flash, his voice rang out faintly.

“Come back alive. You hear me?”

*Fwoooosh.*

An overwhelming flash of light swallowed the space around them.
```
