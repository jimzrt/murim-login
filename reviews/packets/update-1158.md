<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1158.txt",
      "sha256": "da5347a70196e411d9d54f067a4fe60e969b2d3a9ec3be00b3672ecdf2f06d7c",
      "bytes": 12849
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "38863176762d780ae6010695368520340c16a7894df57f87de5399ce896a4996",
      "bytes": 1126
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "7d4396d9a6330a70203162cea821340cc43f73d0c5754dfb3c6a8bfa46a5b17d",
      "bytes": 247107
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "637e5dd883bf02a7f4af5322ba5baec5cc7655c8d2265d9c8733262b9fb86768",
      "bytes": 760
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "4277b8735dcac0cdc3e1c5a678f23bd159c1c618c83df22e8fa94abd1d59fa92",
      "bytes": 867
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "b4b1c9295a6752a251aafbf9182a262229dfe21e12bd6c087f780f8cbfac3228",
      "bytes": 668
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6a26832721aea7fc90963534d804d8acd044fa48b7b7341de783740e0eeb3edd",
      "bytes": 1709
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "840117caf84e42d027de93e858ab05752477adbd2837b95f90f8cb0c01bdc538",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2cf1fde5dbf865897b3caf0136bb60cad574dbf3ce03be66f6e4ae675193cb8d",
      "bytes": 293256
    }
  ],
  "estimated_tokens": 9454
}
-->

# Durable State Update — Chapter 1158

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
1 and safe_through 1158. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1158. Profile updates may replace only one
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
  "chapter": 1158,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1158,
    "continuity_sources": [1158],
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
    "Morgoth’s three-day deadline is still running; his demand for Cheon Taemin and Jin Taekyung as tribute remains in effect.",
    "Cheon Taemin remains unconscious in a recovery capsule in a hidden Pentagon chamber.",
    "Jin believes Cheon Taemin was the Martial God and The Helper, and suspects Asmodeus was not completely erased; these identities and suspicions are unconfirmed.",
    "Jin has ordered World Hunter Federation forces to mobilize for Moscow against Morgoth and his monsters, but intends to go alone.",
    "Code Name Blue is Jin Taekyung; someone who looks like him has apparently escaped through Area 52.",
    "Chuck Hagel was alone when Jin, Johnson, and Choi reached the surface."
  ],
  "continuity_sources": [
    1156,
    1157
  ],
  "open_questions": [
    "Were Cheon Taemin, the Martial God, and The Helper the same person?",
    "Was Asmodeus completely erased?",
    "Who escaped through Area 52 in Jin’s likeness?",
    "What will happen when Morgoth’s three-day deadline expires?"
  ],
  "safe_through": 1157,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 마법사     | **mage**              |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 구천 | **Nine Springs** | Euphemism for the realm of the dead. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 진태경 | 도플갱어 | enemy | you; the Doppelganger | blunt and informal | Jin directly challenges the Doppelganger and demands to know what it wants. |
| 도플갱어 | 진태경 | enemy | you | measured and informal | Replies to Jin’s taunt without using a name or title. |
| 노인 | 진태경 | older opponent to younger opponent; no family relation established | you | calm, familiar speech | The old man addresses Taekyung as 자네 while testing him. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1157
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 1153
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger was a Demon Realm being capable of regenerating in new bodies and was erased by Jin Taekyung.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** It speaks with theatrical, grandiose confidence, taunting opponents in polished, self-important phrasing.
- **Relationships:** It claims to have served Demon King Asmodeus as its master and acted on his order, regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 1154
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1157
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he protects those he cherishes and is learning to face the fear of leaving them in danger without letting it paralyze him.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the Skeleton King a friend; he trusts Sama Pyo despite suspecting his betrayal, was regarded as a worthy successor by Peng Cheolhu, and received the Martial God’s message through the Bow Saint.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1157
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃1158화



그곳은 폐허였다.

굳이 또 다른 표현을 더 하거나 뺄 필요조차 없는, 그저 완전한 폐허.

하지만 불과 십여 초 전, 불현듯 터져 나온 섬광과 함께 모습을 드러낸 어느 한 남자의 생각은 조금 달랐다.

‘무덤.’

그것이 남자가 처음으로 떠올린 생각이었다.

주위를 둘러본 순간, 아니 눈을 뜨기도 전에 느낄 수 있었다. 새벽녘 자욱한 안개처럼 사방을 잠식한 죽음의 기운을. 먹구름에 가로막혀 빛 한 줄기 들어오지 않는 이 거대한 무덤 곳곳에서, 수많은 원혼(冤魂)이 내지르는 비명을.

“……그렇겠지.”

씁쓸하게 중얼거린 남자는 이내 지면을 박차고 쏘아졌다.

쐐애애액!

화살처럼 나아가는 신형을 따라 휘몰아치는 마력(魔力) 때문일까, 이에 반응한 원혼들이 비명을 멈추고 하나둘씩 그를 따라오기 시작했다.

“쫓아오지 마라. 이 몸은 너희의 적이 아니야.”

우우웅.

거친 바람 소리 너머, 원혼들의 대답을 들은 남자가 고개를 끄덕였다.

“그래, 그곳으로 간다.”

우웅-

“너희들의 뜻이 정 그렇다면…… 좋아, 허락하마. 잠시 함께하는 것도 나쁘진 않겠지.”

만약 평범한 사람이 이 광경을 보았다면, 그 순간 두 가지 일로 놀랐을 것이 분명했다.

첫 번째는 정신이상자처럼 보이는 남자의 행동에.

두 번째로는 그 정신이상자가 전 세계 모두가 아는 유명인이라는 사실에.

하지만 이미 죽어 원혼이 된 이들은 달랐다. 남자가 원혼들의 존재와 목소리를 느끼고 들을 수 있듯이, 원혼들 역시 남자의 실체를 볼 수 있었다.

그들은 분명 다르지만, 죽음이라는 단어로 이어져 있는 존재였으니까.

“알아. 억울하겠지. 구해 주지 못해서 미안하다.”

남자는 혼잣말처럼 말을 이었다.

“그럴 리가. 너희는 아무 잘못도 없어. 이건 그저 단순한 불행일 뿐이야. 누구에게나 찾아올 수 있는.”

“신이나 천국이 정말 존재하냐고? 그건 왜?”

“……자식이라, 그렇군. 하지만 걱정하지 마. 그 정도로 어린아이라면 천국에 갔을 테니까. 아니, 분명히 그럴 거야.”

“신이 어떻게 생겼는지는 몰라. 너무 오래전 일이라 기억이 좀 흐릿하거든.”

“거기 너, 방금 그 말 취소해. 이 몸께서는 네 녀석이 감히 쳐다도 못 볼 만큼 위대한 존재시다. 단지 기억력이 조금 안 좋을 뿐이야.”

“그래, 제기랄. 맞아. 사실 아무런 기억도 안 나. 하지만 어느 이상한 녀석과 함께하기 시작한 후부터는 종종 기시감을 느끼고는 하지. 마치 과거에 몇 번이나 비슷한 상황을 겪었던 것처럼 말이야.”

“나름대로 진지하게 생각해 봤는데, 아마도 나 역시 한때 너희와 같은 인간이었을 거야. 분명히 지금처럼 아주 고귀하고 훌륭한…… 빌어먹을. 다들 좀 조용히 해 봐. 중요한 얘기 중이잖아.”

“이런, 너한테 말한 게 아니니까 울지 마. 몇 살이지? 부모는?”

“……알겠어. 약속은 못 하겠지만 네 부모님을 찾게 되면 꼭 만나게 해 주마.”

남자는 계속해서 나아가며 원혼들과의 대화를 이어 나갔다.

이제 막 성인으로서 첫발을 내디딘 청년. 스스로 죽음을 인정하고 사후세계에 대해 묻는 노인. 자식을 잃은 부모와, 부모를 잃어버린 아이.

순식간에 바뀌는 풍경 속에서 그들은 끊임없이 속삭였다. 예고도 없이 들이닥친 죽음에 억울함과 분노를 느끼고, 슬퍼하는 동시에 두려워했다.

그리고 남자는 그들의 목소리를 단 한 번도 외면하지 않았다.

그는 왕이었으니까.

한순간에 모든 것을 잃고 구천을 떠돌게 된, 그리하여 자신의 백성이 된 그들을 인도할 자격과 의무를 갖춘 유일한 존재였으니까.

하지만 이 기묘한 대화를 통해 위로와 안정을 얻는 것은, 비단 원혼들만이 아닐지도 몰랐다.

“왜 이곳에 왔냐고? 흠, 아주 좋은 질문이군. 이건 세상에서 가장 잘생기고 훌륭한 어느 영웅으로부터 시작되는 대서사시야.”

남자는 앞길을 가로막은 폐허를 뛰어넘으며 말을 이었다.

“그 영웅은 다재다능했어. 엄청나게 강한 데다가 고결한 마음을 갖고 있었지. 다만 그런 능력에 비해 주위에는 온통 멍청하고 부족한 놈들투성이였는데, 어느 날 그중에서도 가장 심각한 얼간이가 곤란한 상황에 처해 있다는 사실을 알게 됐어.”

하지만 그 영웅은 얼간이를 도울 수 있는 가장 확실한 해결책을 알고 있었다. 그건 오직 그만이 할 수 있는 일이었다.

왜냐하면, 영웅이니까.

“영웅이 고뇌에 잠겨 있을 때, 술과 담배라면 환장하는 어느 무식한 놈이 그러더군. 인간은 보고 싶은 대로 보고, 믿고 싶은 것만 믿는다고. 그래서 영웅은 잠시 그 얼간이의 모습을 빌리기로 했지.”

그리 어려운 일은 아니었다. 앞서 말했듯 그 영웅은 믿을 수 없을 만큼 다재다능했고, 그가 가진 가장 뛰어난 능력은 ‘흡수’에 있었으니.

“사실 나도, 아니 그 영웅도 자신에게 그런 능력이 있는 줄은 몰랐어. 그런데 막상 해 보니 되더군. 도플갱어(Doppelganger)라는 놈의 본래 능력에 비하면 한참 부족했지만.”

소멸한 몬스터의 마력을 흡수해 오며 강해졌던 본연의 능력 덕분이었을까. 아니면 이미 폭주 단계에 다다른 마력 수치의 영향 때문이었을까.

놀랍게도 인간이 아니었던 영웅은 지금까지 발견하지 못했던 새로운 힘을 갖게 되었고, 몇 번의 워프 게이트를 갈아타며 수천 킬로미터를 이동한 끝에 이곳까지 오게 되었다.

물론 그 과정에서 시끄러운 일도 있긴 했다.

워프 게이트 발동을 거부하던 마법사들을 위협했다거나, 혹은 지금의 모습으로 찍은 셀카를 SNS로 올리고, 의도적으로 동네방네 소문을 퍼트리기도 했다.

하지만 남자에게 있어 그런 사소한 부분은 중요하지 않았다.

이 이야기의 가장 중요한 화룡점정(畵龍點睛)이 남아 있었으니까.

“너희들 중 대부분은 처음부터 눈치챘겠지. 그래, 맞아. 이 몸이 바로 그 영웅이시다.”

솨아아아.

순간 내려앉은 정적에, 비장한 얼굴로 선언한 남자가 눈을 깜빡였다.

“왜 다들 아무 말도 없어? 꼭 죽기라고 한 것처럼, 아니 너희들은 이미 죽긴 했군.”

“뭐? 생각지도 못했다고? 그럴 리가. 시작부터 복선이 완벽했잖아. 분명히 세상에서 제일 잘생기고 훌륭하다고- 제기랄. 됐다. 멍청한 인간 놈들 같으니.”

그때였다. 투덜거리던 남자가 문득 걸음을 멈춘 것은.

“……벌써 여기까지 왔나.”

작게 중얼거린 그는 어느덧 뒤바뀐 풍경을 바라보았다.

마치 누군가가 세상을 구분하는 선을 그은 것처럼, 이전까지와는 달리 칠흑빛을 띤 대지가 고작 몇 걸음 앞에 놓여 있었다.

우웅, 우우우우웅-

그리고 동시에, 남자를 둘러싼 수많은 원혼들이 비명을 토해 냈다.

지금까지와는 비교도 할 수 없는, 오직 공포에 가득 찬 비명을.

“그렇게 무서워할 것 없다. 어차피 너희처럼 약한 원혼들은 저곳으로 들어가기 어려워. 물론 애초에 데려갈 생각도 없지만.”

하지만 남자는 달랐다.

마치 뜨거운 불에 덴 듯 몸부림치는 원혼들과 달리, 그는 저 불길하기 그지없는 칠흑빛 대지에 가까워질수록 자신이 강해질 거라는 사실을 알고 있었다.

‘꾸며 낼 수 있는 건, 결국 겉모습뿐이니까.’

마음속에서 공허하게 흩어지는 뇌까림과 함께, 남자는 허리춤에 꽂혀 있던 검을 뽑았다.

스르릉.

불순물이 섞이지 않은 얼음처럼 투명한 검신.

남자는 그것에 비친 자신의 모습을 말없이 바라보았다.

아니, 지금쯤이면 어디선가 열심히 그를 뒤쫓아오고 있을 누군가의 얼굴을.

“이번에는 한발 늦었다. 이 간악한 인간 놈아.”

남자, 스켈레톤 킹은 낄낄거리며 웃었다. 검신 속에 비친 누군가 역시, 그를 따라 웃고 있었다.

“그래, 앞으로도 계속 그렇게 웃어라. 가뜩이나 못생긴 얼굴로 인상 쓰지 말고.”

진심이었다.

그 얼간이에게는, 진태경에게는 그럴 자격이 있었으니까.

“그럼, 간다.”

닿지 않을 마지막 인사와 함께, 스켈레톤 킹은 힘주어 발걸음을 옮겼다.

검신에서 흘러나오는 빛을 횃불 삼아, 마력이 들끓는 죽음의 땅으로 향하며 생각했다.

‘희생이라, 이것도 나쁘진 않군.’

설령 죽더라도 후회는 없을 것이다.

그가 스켈레톤 킹도, 스톤 킹도 아닌 진태경의 모습으로 장렬한 최후를 맞은 뒤에는 모든 인류가 깨닫게 될 테니까.

진태경을 넘기면 파괴와 학살을 멈추겠다는 몬스터의 약속을 믿었던 자신들이 얼마나 어리석었는지를.

그리고 이 재앙에서 벗어날 유일한 방법이 무엇인지를.

스아아아.

칠흑빛 대지 위에 흐르는 자욱한 안개가, 서서히 멀어지는 그의 뒷모습을 집어삼켰다.



* * *



모르고스는 아주 먼 옛날 들었던 격언을 떠올렸다. 때때로 어떤 종류의 호기심은, 사람의 목숨을 단축시킨다는 그 말을.

그는 인간 사회에 섞여 있을 때 이 말을 처음 들었고, 매우 큰 흥미로움을 느꼈다.

인간과 달리, 드래곤(Dragon)이란 종족은 호기심이 없다면 오래 살아갈 수 없는 존재였으니까. 모르고스 자신이야말로 그 대표적인 예시였다.

그는 늘 호기심이 많았다.

해츨링(Hatchling)에 불과하던 시절부터, 아니 알을 깨고 나오기 전부터 그랬다.

아마도 그래서였을 것이다. 모르고스가 여타의 드래곤들과는 궤를 달리하는 존재로 거듭난 것은.

최고의 수준을 충족하지 않는 한, 그의 호기심은 멈출 줄을 몰랐다.

인간은 물론, 드워프와 엘프를 포함한 여러 이종족까지. 그는 오직 호기심에 이끌려 그들과 아득한 시간을 함께했고, 배움과 동시에 베풀며 군림하기도 했다.

아무리 겉모습과 장소를 바꾸어도, 모르고스는 타고난 지배자였다.

태어난 지 불과 천 년도 되지 않아 드래곤 로드(Dragon Lord)로 선출된 것이 바로 그 예였다.

일족의 자랑이자 세상의 왕.

그는 누구보다 완전하고도 절대적인 존재였다.

단 하나, 해결하지 못한 유일한 호기심만 아니었다면 분명 그러했을 터였다.

‘마계(魔界).’

모든 몬스터들의 고향. 맑은 강물 대신 독과 시체가, 죽음이 흐르는 악마들의 땅.

미지에 대한 호기심은 날이 갈수록 깊어졌고, 모르고스는 그렇게 금기시된 영역에 첫걸음을 내디뎠다.

‘그래, 그게 모든 것의 시작이었지.’

하지만 어째서일까. 아주, 무척이나 오랜 시간이 흘렀음에도 모르고스의 마음속을 가득 채운 호기심은 사그라지지 않았다.

그리고 그중에는, 인간들 사이의 격언처럼 정말 그의 수명을 단축시킬지도 모르는 의문이 포함되어 있었다.

‘아스모데우스여, 그대는 왜 하필 나를 선택했지?’

깊이를 알 수 없을 만큼 방대한 지식과 힘을 가진 모르고스였으나, 정작 자신이 왜 지금의 이 세상에 오게 되었는지는 몰랐다.

단지 어느날 저 머나먼 별과 공간 너머로 부름을 받았고, 그에 응했을 뿐.

그렇기에 더더욱 이해가 되지 않았다.

자신은 다른 이들과 달리 마왕 아스모데우스에게 충성을 다 하지도, 그를 위해 목숨을 바칠 생각도 없었으니까.

‘게다가, 이 세상에 존재하지 않는 그대가 어떻게 이와 같은 무대를 마련할 수 있던 거지?’

그러나 모르고스는 이 의문에 대해 깊게 파고들지 않았다.

아니. 정확히 말하자면, 적어도 지금 당장은 그래야 했다.

그가 진심으로 만남을 원했던 손님이, 지금 막 자신의 궁전으로 찾아왔기에.

“들어오라, 영웅이여.”

왕좌에서 일어난 모르고스는 기쁜 마음으로 첫 손님을 맞이했다.
```

## Final English reading copy

```markdown
# Chapter 1158

It was a ruin.

A complete ruin. There was no need to add or subtract a single word.

But the man who had appeared in a sudden flash of light barely ten seconds ago saw it a little differently.

*A grave.*

That was the first thought that came to him.

He could feel it the moment he looked around—or even before he opened his eyes. The aura of death swallowing everything around him like a thick fog at dawn. The screams of countless vengeful spirits rising from every corner of this enormous grave, where not a ray of light could penetrate the clouds overhead.

“……I suppose so.”

The man muttered bitterly, then kicked off the ground and shot forward.

*Fwoooosh!*

Perhaps it was the magical power swirling in his wake as he streaked forward like an arrow. The spirits reacted to it, stopped screaming, and began following him one by one.

“Don’t follow me. I’m not your enemy.”

*Whoooom.*

Beyond the howl of the wind, the man heard the spirits’ answer and nodded.

“Fine. I’ll go there.”

*Whooom—*

“If that’s what you really want…… Fine, I’ll allow it. There’s no harm in keeping you company for a little while.”

If an ordinary person had seen this, they would surely have been surprised by two things.

First, by the man’s behavior, which made him look insane.

And second, by the fact that this madman was famous all over the world.

But the spirits were different. Just as the man could sense their presence and hear their voices, they could see him as he truly was.

They were certainly different kinds of beings, but they were linked by the word *death*.

“I know. It’s unfair. I’m sorry I couldn’t save you.”

The man continued, as if talking to himself.

“That’s impossible. You did nothing wrong. It was just a simple misfortune. Something that can happen to anyone.”

“You’re asking whether God or heaven really exists? Why?”

“……Your child, huh? I see. But don’t worry. A child that young would have gone to heaven. No—they definitely did.”

“I don’t know what God looks like. It was so long ago that my memory’s a little hazy.”

“You there. Take that back. I’m a great being, far beyond the likes of you. My memory’s just a little bad, that’s all.”

“Yeah, damn it. You’re right. I don’t remember a thing. But ever since I started traveling with a strange fellow, I sometimes get déjà vu. Like I’ve been through something similar several times before.”

“I’ve given it some serious thought, and I think I must have been human once, too. An incredibly noble and excellent human, just like I am now—damn it. Everyone, quiet down. I’m having an important conversation.”

“Oh, don’t cry. I wasn’t talking to you. How old are you? What about your parents?”

“……All right. I can’t promise, but if I find your parents, I’ll make sure you see them.”

The man continued forward, carrying on his conversation with the spirits.

A young man who had only just taken his first steps into adulthood. An old man who had accepted his own death and asked about the afterlife. Parents who had lost a child, and a child who had lost their parents.

The scenery changed in an instant, but the spirits never stopped whispering. They were indignant and furious at the death that had struck without warning, grieving even as they trembled with fear.

And the man never once turned away from their voices.

Because he was their king.

The only being with the right and duty to guide those who had lost everything in an instant and now wandered the Nine Springs—those who had become his people.

But perhaps the spirits weren’t the only ones finding comfort and peace in this strange conversation.

“Why did I come here? Hmm, that’s an excellent question. This is an epic tale that begins with the most handsome and excellent hero in the world.”

The man leaped over the ruins in his path and continued.

“The hero had many talents. He was incredibly strong and had a noble heart. But for all his abilities, he was surrounded by idiots and incompetents. Then one day, he learned that the biggest fool of them all had gotten himself into trouble.”

But the hero knew the surest way to help the fool. It was something only he could do.

Because he was a hero.

“While the hero was deep in thought, some ignorant bastard who was crazy about booze and cigarettes told him that people see what they want to see and believe what they want to believe. So the hero decided to borrow the fool’s appearance for a while.”

It hadn’t been all that difficult. As he’d said, the hero was unbelievably talented, and his greatest ability was “absorption.”

“Actually, I didn’t know I had that ability. No, neither did the hero. But when he tried it, it worked. It wasn’t nearly as good as the Doppelganger’s original ability, though.”

Was it because of his innate ability to grow stronger by absorbing the magical power of monsters that had been destroyed? Or was it because his magical power levels had already reached the point of going berserk?

Amazingly, the hero, who wasn’t human, had gained a new power he’d never discovered before. After traveling thousands of kilometers by way of several Warp Gates, he had made it here.

Of course, there had been some trouble along the way.

He’d threatened the mages who refused to activate the Warp Gate. Or he’d taken a selfie in his current appearance, posted it on social media, and deliberately spread the word far and wide.

But none of those little things mattered to the man.

The grand finale—the most important part of this story—was still to come.

“Most of you figured it out from the start, didn’t you? Yes, that’s right. I am that hero.”

*Fwoosh.*

In the sudden silence, the man blinked after making his solemn declaration.

“Why is everyone so quiet? You’d think you were dead. Oh, right. You are dead.”

“What? You didn’t see it coming? That’s impossible. The foreshadowing was perfect from the start. I said I was the most handsome and excellent man in the world—damn it. Forget it. You stupid humans.”

That was when the grumbling man suddenly stopped walking.

“……I’m already here.”

He murmured and looked at the scenery, now completely transformed.

As if someone had drawn a line dividing the world, a pitch-black landscape lay only a few steps ahead, starkly different from everything behind him.

*Whooom. Whoooooom—*

At the same time, the countless spirits surrounding him let out their screams.

Screams filled with a terror unlike anything they had shown before.

“Don’t be so afraid. Weak spirits like you would have a hard time entering that place anyway. Not that I was planning to take you with me in the first place.”

But the man was different.

The spirits writhed as if burned by fire, but he knew that the closer he got to that ominous, pitch-black landscape, the stronger he would become.

*In the end, only appearances can be faked.*

As the words echoed emptily in his mind, the man drew the sword tucked at his waist.

*Shing.*

Its blade was clear as untainted ice.

The man silently gazed at his reflection in it.

Or rather, at the face of the person who was probably chasing him as fast as he could somewhere out there.

“You’re a step too late this time, you wily human bastard.”

The man—the Skeleton King—snickered. Someone reflected in the blade snickered along with him.

“Yeah, keep smiling like that. Don’t scowl with that ugly face of yours.”

He meant it.

That fool—that Jin Taekyung—deserved to smile.

“Then, here I go.”

With a final farewell that would never reach him, the Skeleton King took a firm step forward.

Using the light spilling from his sword as a torch, he headed for the land of death, where magical power churned, and thought:

*Sacrifice, huh? This isn’t so bad.*

Even if he died, he wouldn’t regret it.

After he met his glorious end in the form of Jin Taekyung—not the Skeleton King or the Stone King—all of humanity would understand.

They would understand how foolish they had been to believe the monsters’ promise to stop the destruction and slaughter if they handed over Jin Taekyung.

And they would understand the only way to escape this catastrophe.

*Fwoooosh.*

The dense fog drifting over the pitch-black land swallowed his retreating figure.

* * *

Morgoth recalled an old saying he’d heard long ago: Sometimes, a certain kind of curiosity can shorten a person’s life.

He’d first heard it while living among humans, and it had fascinated him.

Unlike humans, the Dragon race couldn’t live long without curiosity. Morgoth himself was the perfect example.

He had always been curious.

Ever since he was no more than a Hatchling—or even before he broke out of his egg.

Perhaps that was why Morgoth had become a being unlike any other Dragon.

Nothing short of the very best could satisfy his curiosity.

Humans, of course, but also Dwarves, Elves, and all sorts of other races. Driven by nothing but curiosity, he had spent unfathomable stretches of time among them, learning from them and giving in turn, while also ruling over them.

No matter how often he changed his appearance or location, Morgoth was a born ruler.

His election as Dragon Lord before he had even lived a thousand years was proof of that.

The pride of his race and the king of the world.

He was more complete and absolute than anyone.

At least, he would have been, if not for the one curiosity he had never been able to satisfy.

*The Demon Realm.*

The home of all monsters. The land of demons, where poison, corpses, and death flowed in place of clear rivers.

His curiosity about the unknown deepened with every passing day, until Morgoth took his first step into that forbidden realm.

*Yes. That was where it all began.*

But why? Even after an extraordinarily long time had passed, the curiosity filling Morgoth’s heart had not faded.

And among his unanswered questions was one that, like the saying among humans, might truly shorten his life.

*Asmodeus, why did you choose me of all people?*

Morgoth possessed immeasurable knowledge and power, but he didn’t know why he had come to this world.

He had simply been summoned from beyond distant stars and space, and answered the call.

That made it all the harder to understand.

Unlike the others, he was not devoted to serving Demon King Asmodeus, nor did he intend to give his life for him.

*Besides, how could you, a being who doesn’t exist in this world, have prepared a stage like this?*

But Morgoth did not delve deeply into these questions.

No. To be precise, he had to put them aside for now.

The guest he had truly wanted to meet had just arrived at his palace.

“Come in, hero.”

Morgoth rose from his throne and welcomed his first guest with delight.
```
