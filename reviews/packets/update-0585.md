<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0585.txt",
      "sha256": "7a735ce04fc6c2adccc5efa86dc8a7315f8363ada788f5a45a0fbacd43bf23e2",
      "bytes": 14826
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "75c5b62769452698481215c1ab21d4eb4b6633aaa313ccc980a9293d0d234ae3",
      "bytes": 2668
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bc08995260a037227177c4506d04922f0532db53a950b4181e90e51ea12f3e96",
      "bytes": 183537
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5ad4bf6f1268cd941132b88b525ad692bf13f6f54c09e0633306f72c66a3d232",
      "bytes": 553
    },
    {
      "path": "characters/Hwa-jong.md",
      "sha256": "f67015d2c6940334cffa8ebbfb1f1c8cbc278a53acc1ac6829b3a347cdf8400d",
      "bytes": 665
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "d60ee15cc1d40f58b50abbb3712b22ef7c7aca28f49fc915b843befdcd902bdd",
      "bytes": 1702
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "4367d7c6a42bb0b7b439b1f8af9e1d9ed6bfc4e7344ced78d5efc15013e39c3e",
      "bytes": 713
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ec3a0a8b45b6a8cea41b2328fa0f4ae755f7d8b4e97890dc46e1bbad0e28ca99",
      "bytes": 180828
    }
  ],
  "estimated_tokens": 10401
}
-->

# Durable State Update — Chapter 585

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 585. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 585. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 585,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 585,
    "continuity_sources": [585],
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
    "Song Cheonwoo says Cheon Taemin suddenly collapsed more than twenty years ago and has remained unconscious, but no one knows why.",
    "Song Cheonwoo and Lee Jungryong concealed Taemin's condition, waited two years, conducted experiments, and purged aides who knew the truth.",
    "Hwa-jong was not told about Taemin's condition and remains loyal to Choi Minwoo.",
    "Song claims Taemin is still alive, but his location is unknown and Area A is only suspected.",
    "Choi Minwoo has confirmed Song's account enough to treat Taemin's status as genuine while continuing to investigate.",
    "Busan's Kraken has been eliminated, but more than one thousand Mermen remain across Haeundae and Gwangalli while the Peace Guild and other forces contain the disaster.",
    "Go Jun seized Song Cheonwoo's children as leverage and used the threat to force Song to attack Choi Minwoo.",
    "Go Jun used an S-grade Magic Gem to artificially cause the Busan Monster Wave and sent Kim Ho-jung to Busan.",
    "Go Jun intends to kill Choi Minwoo through Song Cheonwoo and may be relying on another unidentified being.",
    "Song Cheonwoo was killed after falling into an abyss and being attacked by an unidentified monster; the unused object in his pocket released darkness that became light after his death.",
    "Kim Hwajong forced Behemoth to kneel by disabling its two forelegs, but Behemoth gravely injured him while Choi Minwoo escaped; a flash from midair interrupted the monster's final attack."
  ],
  "continuity_sources": [
    584,
    583
  ],
  "open_questions": [
    "What caused Cheon Taemin's collapse, and what happened during his more than twenty years of unconsciousness?",
    "Is Cheon Taemin actually being kept in Area A of Ares Guild headquarters?",
    "What is the unidentified being involved in Go Jun's plan, and is it connected to the monster that killed Song Cheonwoo?",
    "What was the object Song Cheonwoo kept unused in his pocket, and what did its release of darkness and light accomplish?",
    "Did Choi Minwoo and Kim Hwajong survive the Pyeongchang confrontation, and what caused the final flash?"
  ],
  "safe_through": 584,
  "temporary_decisions": [
    "Use Yeti's Winter Range for 예티의 겨울 산맥, Behemoth for 베히모스, and Behemos for 베헤모스.",
    "Use Stone King for 스톤 킹 and Skeleton King for 스켈레톤 킹.",
    "Use Area A for A구역.",
    "Use Hwa-jong for 화종.",
    "Use Hero's Soul for 영웅의 혼, Hyung for 형님, S-grade Magic Gem for S급 마정석, Hell Fire for 헬 파이어, and Hellfire Mage for 겁화의 마법사."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 김화종    | **Kim Hwajong**   |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 산서     | **Shanxi**             |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 화종 | **Hwa-jong** | Butler Kim's personal name. |
| 평화 | **Peace Guild** | Guild name. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 도련님 | **Young Master** | Address used for Team Leader Choi by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 탈진 | **Exhaustion** | System status effect caused by exhausting all internal energy while severely injured. |
| 쓰촨 | **Sichuan** | Variant spelling used for the region associated with the pattern Jin recognizes. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 부산 | **Busan** | City where the Haeundae Gate crisis occurs. |
| 베히모스 | **Behemoth** | Mythical monster emerging from the Pyeongchang Gate. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 팀장 | 중년인 | Hunter_team_leader_to_stranger | Boss | casual and polite | The Team Leader mistakes disguised Song for an ordinary raid customer and warns him not to proceed. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 584
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hwa-jong.md

# Hwa-jong (화종)

- **Safe through:** Chapter 584
- **Aliases:** Butler Kim
- **Role:** Hwa-jong is Choi Minwoo's loyal butler and personal escort who remained behind after losing his left arm to fight Behemoth and rendered its two forelegs unusable.
- **Personality:** Loyal, vigilant, and uncompromising toward perceived threats to Choi Minwoo.
- **Voice:** Formal and deferential toward Choi Minwoo, cold and openly hostile toward Song Cheonwoo.
- **Relationships:** Hwa-jong serves Choi Minwoo and was formerly close to Song Cheonwoo, but their relationship ended over loyalty and ambition.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 551
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 584
- **Aliases:** Butler Kim
- **Role:** Kim Hwajong is a Level 80 mage known as Butler Kim and Choi Minwoo's loyal butler and personal escort who remained behind after losing his left arm to fight Behemoth and rendered its two forelegs unusable.
- **Personality:** Gentle and composed as Butler Kim, but retains a fiery temperament and a habit of swearing.
- **Voice:** Gentle and measured
- **Relationships:** Kim Hwajong formerly instructed Im Chunsoo, who remains terrified of and obedient to him, and serves Choi Minwoo as butler and personal escort, having become Choi's only family.

## Korean source

```text
＃585화



쐐애애애액!

머리 위로 울려 퍼지는 맹렬한 파공성에, 비명을 지르며 뿔뿔이 흩어지던 수천 명의 발걸음이 우뚝 멈췄다. 하늘을 올려다본 어느 관광객의 입술 사이로 넋 나간 목소리가 흘러나왔다.

“……어?”

그것은 비단 한 사람이 품은 의문이 아니었다.

마수를 피해 도망치던 민간인들, 마수를 저지하기 위해 출동한 수백의 지원 병력, 길드장의 마지막 소망을 따라 다급히 산 아래로 내려가던 평화 길드의 헌터들까지. 모두가 그 광경을 바라보았고, 같은 의문을 떠올렸다.

‘저게 뭐지?’

하지만 그들은 각각 다른 시각과 시야를 지니고 있었다. 민간인들이 허공을 가로지르는 빛줄기에 순수한 의문을 품었다면, 지원 병력에 포함되어 있던 상위 헌터들은 찰나의 순간 까마득한 상공에서 강대한 마나의 흐름을 느꼈다.

동시에 그보다 더 가까운 산 중턱에 있던 평화 길드원들은 머리 위를 가로지르는 빛줄기가 어떻게 허공에서 나타났는지 알아차렸다.

‘……텔레포트(Teleport)?’

누가, 어떻게, 왜.

수많은 사람들의 머릿속에 떠오른 숱한 의문들. 그러나 이 모든 광경을 누구보다 똑똑히 보고 느낀 것은 김화종이었다.

죽음의 끄트머리에 앉아 있던 노집사는, 마력으로 이루어진 검은 안개를 짓누르며 퍼져 나가는 푸른 빛줄기의 정체를 깨달았다.

‘저것은.’

어떤 것보다 파괴적이며, 순수한 힘.

화염(火焰). 그건 화염이었다.

햇살보다 강렬하고, 태양만큼이나 격렬한 화염이 빛줄기가 되어 하늘을 가로지르고 있었다. 문득 제대로 바라볼 수 없을 정도로 눈부신 섬광 속에 있을 누군가의 얼굴이 흐릿한 시야에 스치는 듯했다.

‘그래, 자네로군.’

노집사의 입가에 서린 미소가 짙어진 그때, 신화를 딛고 일어난 태고의 마수가 자신을 향해 쏘아지는 빛줄기를 향해 거대한 아가리를 벌렸다.

콰아아아아아-

바람이 갈라지고, 공기가 흩어졌다. 산을 집어삼킬 듯 벌어진 입 안에서 심연(深淵)을 닮은 기운이 소용돌이쳤다.

그러나 빛줄기는 멈추지 않았다. 더욱더 날카롭고, 거대해진 그것은 청백색의 빛을 띤 불꽃으로 화하며 휘몰아쳤다.

고오오오옹.

세상이 멈췄다. 모든 공간과 소음을 집어삼키며 나아간 두 개의 기운이 격돌했다.

그리고 다음 순간, 김화종은 볼 수 있었다. 들을 수 있었다.

화아아아악!

푸른 하늘 아래 갈가리 찢겨 나가는 어둠을.

막아서는 모든 것을 불태우며 질주하는 청백색 화염과, 적막이 가득한 눈부신 세상에서 또렷하게 울려 퍼지는 한 사람의 목소리를.

“일섬(一殲).”

공간이 일그러졌다. 유성처럼 떨어져 내린 미증유(未曾有)의 화염이 채 다물어지지 못한 베히모스의 아가리를 관통했다.

천둥과도 같은 단말마와 함께 기울어지는 마수의 모습을 보며, 노집사는 고통도 잊은 채 소리 내어 웃었다.



* * *



천하제일의 고수라도, 신화에서나 등장할 법한 고대의 마수라 할지라도 죽음을 피할 수는 없다. 특히 온 힘을 다한 일섬이 입을 통해 전신을 관통한 경우라면 더더욱.

- 어…떻…….

지금껏 본 적도, 들어 본 적도 없는 마수의 눈동자에 의문과 죽음이 동시에 내려앉았다. 공허하게 나를 바라보던 놈의 거대한 동체가 천천히 기울어졌다.

쿠구구구궁!

생명이 빠져나간 몸뚱어리가 쓰러지자 산 전체가 몸을 떨었다. 동시에 사방에서 피어오르는 엄청난 크기의 먼지구름 사이에서, 나는 파도처럼 밀려드는 고통과 피로를 참기 위해 이를 악물어야 했다.

‘쓰러져서는 안 돼.’

일섬은 시전자의 모든 힘을 일거에 쏟아내는 양날의 검.

하지만 아직은 아니다. 적어도 지금 같은 상황에서는 쓰러질 수 없다. 그나마 다행인 것은, 나는 평범한 사람들과는 다른 유별난 힘을 갖고 있다는 것이었다.

띠링. 띠링. 띠링.



- [Lv.150 베히모스]를 처치하셨습니다!

- 막대한 경험치와 명성을 획득하셨습니다!

- 레벨 업!

- 상태 이상, [탈진]이 해제되었습니다!

- 상태 이상, [공력 소진]이 해제되었습니다!

- 레벨 업의 효과로 일부 피로와 상태 이상이 사라집니다!

.

.

.



‘빌어먹을.’

나는 비틀거리는 신형을 간신히 다잡았다.

레벨 업은 분명히 시스템의 사기적인 기능 중 하나지만, 중첩되지 않는 이상에야 만능은 아니다. 그만큼 현재 내 육체와 정신에 축적된 피로는 막대했고, 손발은 일섬을 사용한 후유증으로 마치 감전이라도 된 것처럼 저릿저릿했다.

하지만 멈출 수도 없고, 쓰러질 수도 없었다. 나는 레벨 업과 함께 단전에 차오른 공력을 끌어올려 전방을 향해 발출했다.

퍼엉!

압축된 공기가 터져 나가며 먼지구름이 흩어진다. 비로소 깨끗해진 시야 너머로, 새하얀 뼈마디로 뒤덮인 둥근 형체가 모습을 드러냈다.

저벅. 저벅.

한 걸음. 한 걸음. 난장판이 된 지면을 가로지를 때마다 가슴이 거세게 뛰었다. 가쁘게 내뱉는 숨결에는 숨길 수 없는 긴장과 두려움이 섞여 있었다.

맞다. 나는 곧 마주하게 될 누군가의 모습이 두려웠다. 그가 내 바람과는 다른 모습을 하고 있을까 봐. 준비되지 않은 이별 인사를 건넬까 봐.

툭. 촤르르륵.

조심스럽게 손을 대자, 뼈로 이루어진 막이 녹아내리듯 흩어졌다. 그리고 비로소 볼 수 있었다. 어두운 얼굴의 금발 외국인과, 그에게 기대어 꺼질 듯한 호흡을 이어 가고 있는 반백의 중년인을.

‘이건.’

순간, 심장이 멈춘 듯했다.

비록 찰나였지만 상황을 알아차리는 것은 어렵지 않았다. 스켈레톤 킹의 발치에서 힘없이 굴러다니는 최상급 포션 병은 텅 비어 있었고, 겉보기에는 아무런 문제 없이 회복된 듯한 중년인의 전신에서는 이미 서서히 힘이 빠져나가고 있었다.

나는 눈앞이 아득해지는 것을 느끼며 입을 열었다.

“……김 집사님.”

내 부름에 반쯤 감겨 있던 눈꺼풀이 잘게 떨렸다. 꺼질 듯한 눈동자와 시선을 마주하자, 피에 젖은 입꼬리가 부드럽게 올라갔다.

“자네 왔나.”

“……!”

“그래. 자네일 줄 알았지. 그 빛, 정말로 따뜻했거든.”

나는 신음을 참기 위해 이를 악물었다. 이미 김 집사는 자신에게 닥친 모든 상황을 받아들이고 있었다. 평소와는 다른 말투도 그 때문일 것이다.

지금 내 눈앞의 이 남자는 김 집사도, 평화 길드장도 아닌 그저 한 사람의 인간. 김화종으로서 작별 인사를 건네고 있었다.

하지만…….

‘저는 아직입니다.’

난 이 갑작스러운 이별을 받아들일 수 없다. 그를 웃으며 떠나보낼 생각도 없다. 죽음을 앞두고 인간 김화종으로 돌아온 그를 김 집사로, 길드장으로 되돌려 놓기 위해서 무슨 짓이든 할 것이다.

“한데 이제는 좀 춥군. 아까는 참 따뜻했는데.”

나는 희미한 목소리로 중얼거리는 김화종의 손을 붙잡고, 열양지기를 천천히 흘려보내며 대답했다.

“산 위라서 그럴 겁니다. 곧 따뜻해질 거예요.”

“그런가?”

그의 힘없는 물음에 애써 웃었다.

“예. 아직 겨울이잖습니까.”

이내 스며드는 온기를 느낀 김화종이 옅은 웃음을 지었다.

“정말이군. 자네 말대로야.”

“괜찮을 겁니다. 걱정하지 마세요. 제가 다 알아서…….”

순간 말꼬리를 흐릴 수밖에 없었던 건, 먹먹해진 가슴 때문만이 아니었다. 앞서 흘려보낸 공력으로 살핀 그의 몸 상태가 내 말문을 굳게 틀어막았다.

‘이게 도대체…….’

인간의 몸에는 날 때부터 타고난 기운, 즉 선천지기(先天眞氣)가 존재한다. 이는 모든 기운의 근원이자 뿌리나 다름없는 것. 그러나 현재 김화종의 몸에는 그 선천지기가 거의 남아 있지 않았다.

아니, 그조차도 서서히 타들어 가는 중이다.

‘사그라지는 불꽃처럼.’

과거 적천강 역시 하남에서 선천지기가 손상되긴 했지만 이 정도는 아니었다. 지금의 김화종은 경우에는 돌이킬 수 없을 지경이다.

공력을 통해 관조한 몸 상태만으로도 충분히 짐작할 수 있었다.

그가, 김화종이 어떤 각오로 베히모스와 맞섰는지. 짙은 어둠에서 기어 올라온 마수의 발을 묶기 위해 무엇을 희생해야 했는지. 그리고…… 하나뿐인 생명을 장작 삼아 타올랐던 것이 누구를 위해서였는지.

“도련님……. 민우는, 그 아이는 무사한가?”

꺼질 듯한 그의 물음에, 나는 애써 밝은 어조로 대꾸했다.

“무사합니다. 산 중턱에서 스치듯 봤었는데 아무 문제 없어요.”

“그래, 다행이군. 정말 다행이야.”

무엇이 그리도 다행입니까. 정작 당신은 이 꼴이 되었으면서.

차마 입 밖으로 내지 못한 질문과 함께 지그시 입술을 깨문 그때, 스켈레톤 킹이 흘려보낸 의념(意念)이 머릿속에 울려 퍼졌다.

- 뼛속까지 스며든 마력을 흡수하고, 최상급 포션을 사용했지만 이미 늦은 후였다. 이 몸이 나섰음에도 어쩔 수 없었어.

안다. 그래서 탓할 수 없었다. 녀석이 최선을 다한 것을 알기 때문에. 비록 녀석의 모든 것은 환영 마법으로 이루어진 허상이지만, 지금 스켈레톤 킹의 얼굴에 떠오른 자책과 슬픔은 진짜였다.

- ……미안하다. 인간.

문득 의문이 들었다. 그건 지금 내가 처한 모든 상황에 관한 의문이었다.

도대체 왜 이 녀석이 사과를 하는 것일까. 며칠 전만 하더라도 함께 식탁에 앉아 밥을 먹고, 웃으며 대화하던 김화종은 회복불능의 상태가 되어 누워 있는 것일까.

그리고 왜. 나는 이런 상황을 막지 못했을까.

‘도대체 왜.’

내게는 힘이 있었다. 재앙을 막고 불행한 죽음을 막을 수 있는 힘이.

어느 날 불현듯 인생에 끼어든 정체불명의 캡슐이 모든 것의 시작이었다. 그것으로 내게 주어진 운명을 바꾸었고, 새롭고 소중한 인연들을 만났다. 그리고 지금, 그 인연 중 하나가 끊어지려 한다. 내 곁을 떠나려 한다.

그런데 나는 왜, 막지 못하는 걸까.

산서에서, 하남에서, 사천에서, 호북에서. 쓰촨에서, 부산에서…….

무림과 현대를 오가며 그토록 수많은 목숨을 살렸는데, 어째서 눈앞에서 떠나려 하는 한 사람은 구하지 못하는가.

‘왜.’

해결할 수 없는 의문과 막막함에 잠겨 가던 그때였다.

스윽, 툭.

파르르 떨리는 주먹 위를, 차가운 손이 덮었다. 김화종이 온기 어린 눈빛으로 나를 바라보며 입을 열었다.

“자네 잘못이 아니야.”

“……!”

“자네는 최선을 다했네.”

흐릿하던 눈동자도, 꺼질 것 같던 목소리도 더는 찾아볼 수 없다. 따뜻하게 나를 위로하는 그의 모습에 숨이 턱 하고 막혔다.

‘회광반조(回光返照).’

죽음의 끝자락에서 마지막으로 피워 올리는 불꽃.

안 된다. 아직은 그를 떠나보낼 수 없다. 이를 악문 나는 김화종의 몸속으로 더욱 강한 공력을 흘려보냈지만, 간절한 바람과는 달리 한계에 다다른 육신에서는 서서히 힘이 빠져나가고 있었다.

‘더, 조금만 더!’

나는 단전에 웅크린 공력을 아낌없이 쏟아부었다. 조금씩 닫혀 가는 혈도를 붙잡고, 그의 몸 깊숙한 곳에서 꺼져 가는 불꽃을 북돋웠다. 하지만 그런 시도에도 불구하고, 마지막은 가파른 속도로 찾아오고 있었다.

“춥군. 자네 말처럼 겨울이라서 그런 건지, 벌써 밤이 되어서 그런 건지 모르겠어.”

그럴 리 없다. 지금 이 순간에도 그의 몸속으로 막대한 열양지기가 흘러 들어가는 중이고, 오후의 태양은 여전히 하늘에 떠 있었으니까.

그러니 김화종에게 찾아온 추위와 어둠은 오직 그만이 느낄 수 있는 것이었다. 목전까지 들이닥친 죽음이 그의 몸을 얼리고, 눈앞을 가린 것이다.

나는 가늘게 호흡하는 노집사를 향해, 더듬더듬 중얼거렸다.

“괜찮습니다. 잠시 후면 최 팀장님도 볼 수 있을 테니까 저만 믿고…….”

턱.

내 손목을 붙잡은 누군가의 손. 어두운 얼굴로 고개를 가로젓는 스켈레톤 킹의 모습에, 나는 비로소 깨달았다. 어떤 말과 행동으로도 한 사람의 마지막을 막을 수 없다는 것을.

이제는…… 놓아줘야 할 때였다.

그가, 김화종이 조금이라도 마음 편히 떠날 수 있도록.

“도련님은, 민우 그 아이는 무사한가?”

어느새 희뿌옇게 물든 눈동자. 힘없는 목소리로 중얼거리는 그 물음은 이미 들었던 것이었지만, 상관없었다. 백 번, 천 번이라도 다시 대답해 줄 수 있다.

“무사합니다. 털끝 하나 다치지 않았습니다.”

“보고 싶군. 마지막으로 한 번만 더…….”

“볼 수 있을 겁니다. 이미 이곳으로 오고 있어요.”

“그게, 정말인가?”

“예. 아, 저기 오네요.”

거짓말이었다. 새빨간, 동시에 새하얀 거짓말.

한바탕 혼란을 휩쓸고 간 이름 모를 산등성이 위에는 오직 우리 세 사람과 마수의 사체뿐이었다.

그러나 김화종은 거짓말이라는 사실을 분간할 수 없었다. 희뿌연 시야와 흐릿한 정신만이 남은 그는 허공으로 손을 뻗었다. 마치 애타게 기다리던 누군가가 자신의 손을 잡아 줄 것처럼.

덥석.

눈짓 섞인 내 부름에, 스켈레톤 킹이 그 손을 굳게 붙잡았다. 노집사의 눈이 반달처럼 휘어지고 입가에는 환한 웃음이 번졌다.

“왔느냐.”

그리고 다음 순간.

“내 손…자.”

한 사람을 위해 타오르고, 이 순간을 위해 꺼지지 않았던 불꽃이 마침내 사그라졌다.

스륵. 툭.

암전(暗轉)이었다.
```

## Final English reading copy

```markdown
# Chapter 585

Kwoooosh!

At the fierce sound of air being torn apart overhead, the footsteps of thousands of people fleeing in every direction came to an abrupt halt. From among the tourists looking up at the sky, a dazed voice slipped past one person’s lips.

“……Huh?”

It was not a question held by only one person.

The civilians fleeing from the monster, the hundreds of support troops dispatched to stop it, and even the Peace Guild Hunters hurrying down the mountain in accordance with their Guild Master’s final wish—all of them watched the scene and thought of the same question.

*What is that?*

But each group had a different perspective and field of vision. While the civilians looked at the streak of light cutting across the sky with simple bewilderment, the high-ranking Hunters among the support troops sensed a powerful flow of mana in the distant sky for the briefest instant.

At the same time, the Peace Guild members on the mountainside, much closer to the scene, realized how the streak of light overhead had appeared out of thin air.

*……Teleport?*

Who? How? Why?

Countless questions flashed through the minds of countless people. But the one who saw and felt the entire scene more clearly than anyone else was Kim Hwajong.

The old butler, sitting at death’s doorstep, realized the identity of the blue streak spreading outward as it pressed down on the black mist made of magic power.

*That is…*

Something more destructive than anything else. Pure power.

Flame. It was flame.

Flame more intense than sunlight and as fierce as the sun itself streaked across the sky as a beam of light. For a moment, within the dazzling flash so bright that he could barely look at it, a face seemed to pass across his blurred vision.

*Yes. It’s you.*

Just as the smile at the corners of the old butler’s mouth deepened, the primordial monster that had risen from myth opened its enormous jaws toward the streak of light shooting at it.

Kwoooooom—

The wind split apart, and the air scattered. Within the jaws opened wide enough to swallow a mountain, an energy resembling an abyss churned.

But the streak of light did not stop. It grew sharper and larger, transforming into a blue-white flame that whipped through the air.

Gooooooong.

The world stopped. Two forces that swallowed all space and sound as they advanced collided.

And in the next moment, Kim Hwajong could see. He could hear.

Fwoooooosh!

Darkness being torn to shreds beneath the blue sky.

Blue-white flames racing forward while burning everything in their path, and one person’s voice ringing clearly through a dazzling world filled with silence.

“One Annihilation.”

Space warped. The unprecedented flames that fell like a meteor pierced through Behemoth’s jaws before they could fully close.

Watching the monster tilt to one side with a death cry like thunder, the old butler forgot his pain and laughed aloud.

* * *

Even the greatest master in the world, even an ancient monster who seemed fit to appear only in myth, could not escape death. Especially not when a full-powered One Annihilation had pierced through its entire body via its mouth.

—Ho…w……

Bewilderment and death settled at once in the eyes of the monster—a creature unlike any ever seen or heard of. Its enormous body, staring blankly at me, slowly tilted.

Krrrrrrrung!

When the body emptied of life collapsed, the entire mountain trembled. At the same time, amid the enormous clouds of dust rising from every direction, I had to grit my teeth to endure the pain and fatigue surging over me like waves.

*I must not collapse.*

One Annihilation was a double-edged sword that poured all of its caster’s power out at once.

But not yet. At least not in a situation like this. I couldn’t collapse now. The one fortunate thing was that I possessed an unusual power unlike that of ordinary people.

> **System**
>
> You have defeated **Lv. 150 Behemoth**!
>
> You have acquired an enormous amount of **EXP** and **Fame**!
>
> **Level Up!**
>
> The Status effect **Exhaustion** has been removed!
>
> The Status effect **Internal Energy Depletion** has been removed!
>
> Some fatigue and Status effects have disappeared due to the effects of **Level Up**!
>
> …
>
> …
> 
> …

*Damn it.*

I barely steadied my staggering body.

Leveling up was certainly one of the System’s most broken features, but it was not omnipotent unless its effects stacked. The fatigue accumulated in my body and mind was that severe, and my hands and feet tingled as though I had been electrocuted from the aftereffects of using One Annihilation.

But I couldn’t stop, and I couldn’t collapse. Along with the level-up, I drew up the internal energy filling my dantian and released it forward.

Boom!

The compressed air burst outward, scattering the dust cloud. Beyond the view that finally cleared, a rounded shape covered in pure white bones appeared.

Step. Step.

With every step I took across the devastated ground, my heart pounded violently. The breath escaping my lips was mixed with tension and fear that could not be hidden.

That was right. I was afraid of the person I was about to face.

I was afraid he might look different from what I wished for. Afraid I might have to say goodbye before I was ready.

Tap. Shrrr…

When I carefully placed my hand against it, the membrane made of bones scattered as though it were melting. And then I could finally see.

A grim-faced blond foreigner, and a middle-aged man with half-gray hair leaning against him, continuing to breathe as though each breath might be his last.

*This is…*

For a moment, it felt as though my heart had stopped.

Though it lasted only an instant, it was not difficult to understand the situation. The bottle of top-grade potion rolling weakly at Skeleton King’s feet was empty, and strength was already slowly leaving the middle-aged man’s entire body, even though he appeared to have recovered without any visible problems.

Feeling my vision grow distant, I opened my mouth.

“……Butler Kim.”

At my call, his half-closed eyelids trembled faintly. When our eyes met—his gaze on the verge of fading—his bloodstained lips curved gently upward.

“You came.”

“……!”

“Yes. I knew it would be you. That light was truly warm.”

I gritted my teeth to hold back a groan. Butler Kim had already accepted everything that had happened to him. That was probably why his tone was different from usual.

The man before my eyes was neither Butler Kim nor the Guild Master of the Peace Guild. He was simply a human being, Kim Hwajong, saying goodbye.

But…

*I’m not ready yet.*

I couldn’t accept this sudden farewell. I had no intention of smiling as I sent him away. I would do anything to return the man who had become Kim Hwajong the human being in the face of death to Butler Kim, to the Guild Master.

“But I’m a little cold now. It was so warm earlier.”

I took Kim Hwajong’s hand as he muttered in a faint voice and slowly sent Scorching Yang Qi into it as I answered.

“It’s because we’re on a mountain. You’ll be warm soon.”

“Is that so?”

I forced a smile at his feeble question.

“Yes. It’s still winter, after all.”

Feeling the warmth seep into him, Kim Hwajong gave a faint smile.

“It really is. Just as you said.”

“You’ll be all right. Don’t worry. I’ll take care of everything…”

I could not finish the sentence. It was not only because my chest had tightened. The condition of his body, which I had examined with the internal energy I sent through him, had sealed my lips.

*What in the world…*

The human body contained an energy possessed from birth: innate qi. It was no different from the source and root of all energy. But almost none of that innate qi remained in Kim Hwajong’s body.

No. Even that was slowly burning away.

*Like a dying flame.*

Jeok Cheongang’s innate qi had also been damaged in Henan in the past, but it had never been this bad. In Kim Hwajong’s case, it had reached the point of no return.

I could tell enough just by observing his condition through my internal energy.

The resolve with which he, Kim Hwajong, had faced Behemoth. What he had sacrificed to tie down the feet of the monster that had crawled up from the depths of darkness. And…

Who he had used his one and only life as kindling for.

“Young Master… Is Minwoo, is that child safe?”

I answered his fading question in as bright a tone as I could manage.

“He’s safe. I caught a glimpse of him on the mountainside, and there’s nothing wrong with him.”

“Yes. That’s a relief. A real relief.”

*What is there to be so relieved about? You’re the one who ended up like this.*

Just as I bit down firmly on my lips, along with the question I could not bring myself to speak, the thought Skeleton King sent out rang through my mind.

—Though I absorbed the magic that had seeped into his bones and used a top-grade potion, it was already too late. Even after this body stepped in, there was nothing I could do.

I knew. That was why I could not blame him. I knew he had done everything he could.

Though everything about him was an illusion created by illusion magic, the guilt and sorrow on Skeleton King’s face were real.

—……I’m sorry, human.

A question suddenly occurred to me. It was a question about everything happening to me right now.

Why was this guy apologizing?

Why was Kim Hwajong, who had been sitting at the table with us, eating and laughing as we talked only a few days ago, now lying here in a state beyond recovery?

And why had I been unable to stop it?

*Why?*

I had power. The power to stop disasters and prevent tragic deaths.

It all began with the mysterious capsule that had suddenly intruded into my life one day. With it, I changed the fate I had been given and met new, precious connections. And now one of those connections was about to be severed. Someone was about to leave my side.

Then why couldn’t I stop it?

In Shanxi, Henan, Sichuan, and Hubei. In Sichuan, and in Busan…

I had saved so many lives while traveling between the Murim and the modern world. So why couldn’t I save the one person about to leave before my eyes?

*Why?*

It was then, as I sank into an irresolvable question and helplessness.

Ssssh. Tap.

A cold hand covered my trembling fist. Kim Hwajong looked at me with warm eyes and opened his mouth.

“It isn’t your fault.”

“……!”

“You did your best.”

His blurred eyes and fading voice were nowhere to be found now. Seeing him warmly comforting me made my breath catch in my throat.

*The final rally.*

The last flame raised at the edge of death.

No. I still couldn’t let him go. Gritting my teeth, I sent even stronger internal energy into Kim Hwajong’s body. But contrary to my desperate wish, strength was slowly leaving the body that had reached its limit.

*More. Just a little more!*

I poured out the internal energy coiled in my dantian without holding anything back. I held open the acupoints that were slowly closing and fanned the flame dying deep within his body.

But despite my attempts, the end was approaching at a frightening speed.

“It’s cold. I don’t know whether it’s because it’s winter, like you said, or because night has already fallen.”

That was impossible. Even now, an enormous amount of Scorching Yang Qi was flowing into his body, and the afternoon sun was still in the sky.

The cold and darkness that had come over Kim Hwajong were things only he could feel. Death that had reached his doorstep was freezing his body and blocking his view.

I mumbled haltingly toward the old butler, whose breathing had grown thin.

“It’s all right. You’ll be able to see Team Leader Choi soon, so just trust me…”

Thud.

A hand seized my wrist. When I saw Skeleton King shaking his head with a dark expression, I finally realized.

No words or actions could stop one person’s final moment.

Now…

It was time to let him go.

So that he—so that Kim Hwajong—could leave with even a little peace of mind.

“Young Master… Is Minwoo, is that child safe?”

His eyes had grown cloudy without my noticing. Though I had already heard the feeble question he muttered, it did not matter. I could answer him a hundred or a thousand times.

“He’s safe. He hasn’t been hurt in the slightest.”

“I want to see him. Just one last time…”

“You’ll be able to. He’s already on his way here.”

“Is that really true?”

“Yes. Ah, there he is.”

It was a lie. A bright red, pure white lie.

On the nameless mountainside swept by a wave of chaos, there were only the three of us and the monster’s corpse.

But Kim Hwajong could not tell that it was a lie. With only his cloudy vision and fading mind remaining, he reached a hand toward empty air.

As though someone he had been desperately waiting for would take his hand.

Grab.

At my call and the look that accompanied it, Skeleton King firmly took that hand. The old butler’s eyes curved like crescent moons, and a radiant smile spread across his lips.

“You’ve come.”

And then, in the next moment—

“My grand…son.”

The flame that had burned for one person and refused to go out for this moment finally guttered.

Sssrrk. Tap.

The world went black.
```
